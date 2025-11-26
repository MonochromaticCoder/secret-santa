import json
import os
from Crypto.Cipher import PKCS1_OAEP
import random
import secrets
import datetime

from config import PARTICIPANTS

if __name__ == "__main__":
    assert len(PARTICIPANTS) == len({x.id for x in PARTICIPANTS}), "Duplicate IDs"
    assert not {
        restriction
        for participant in PARTICIPANTS
        for restriction in participant.cannot_give_to
    }.difference({x.id for x in PARTICIPANTS}), "Draw restrictions contain unknown IDs"
    for participant in PARTICIPANTS:
        if participant.public_key.size_in_bits() != 2048:
            raise Exception(
                f"{participant.id} has an unexpected key size of {participant.public_key.size_in_bits()}"
            )

    random.seed(secrets.token_bytes(64))

    assignment = PARTICIPANTS[:]
    random.shuffle(assignment)
    while not all(
        recipient.id not in {gifter.id, *gifter.cannot_give_to}
        for gifter, recipient in zip(assignment, assignment[1:] + [assignment[0]])
    ):
        random.shuffle(assignment)

    json_assignment = {}
    for gifter, recipient in zip(assignment, assignment[1:] + [assignment[0]]):
        cipher = PKCS1_OAEP.new(gifter.public_key)
        encrypted_recipient = cipher.encrypt(recipient.id.encode()).hex()
        json_assignment[gifter.id] = encrypted_recipient
        print(f"{gifter.id}: {encrypted_recipient}\n")

    os.makedirs("_data", exist_ok=True)
    json.dump(
        {
            "metadata": {
                "generated_at": datetime.datetime.now().isoformat(),
                "repo_url": f"{os.getenv("GITHUB_SERVER_URL")}/{os.getenv("GITHUB_REPOSITORY")}",
                "commit_hash": os.getenv("GITHUB_SHA"),
            },
            "assignments": json_assignment,
        },
        open("_data/assignments.json", "w"),
        sort_keys=True,
    )
