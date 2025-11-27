import json
import os
from Crypto.Cipher import PKCS1_OAEP
import random
import secrets
import datetime

from config import DRY_RUN, PARTICIPANTS

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

    assignments_json = {
        gifter.id: (
            PKCS1_OAEP.new(gifter.public_key)
            .encrypt(b"This is a dry run" if DRY_RUN else recipient.id.encode())
            .hex()
        )
        for gifter, recipient in zip(assignment, assignment[1:] + [assignment[0]])
    }
    print(json.dumps(assignments_json, sort_keys=True, indent=4))

    os.makedirs("_data", exist_ok=True)
    json.dump(
        {
            "metadata": {
                "generated_at": datetime.datetime.now().isoformat(),
                "repo_url": f"{os.getenv("GITHUB_SERVER_URL")}/{os.getenv("GITHUB_REPOSITORY")}",
                "commit_hash": os.getenv("GITHUB_SHA"),
                "run_id": os.getenv("GITHUB_RUN_ID"),
            },
            "assignments": assignments_json,
        },
        open("_data/assignments.json", "w"),
        sort_keys=True,
    )
