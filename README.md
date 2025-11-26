# 🎅 Secret Santa

A Secret Santa assignment system using asymmetric encryption. No single party (including the script runner) can see the assignments.

---

## For Participants

### Step 1: Generate Your RSA Key Pair

1. Visit https://emn178.github.io/online-tools/rsa/key-generator/
2. Set **Key Size** to `2048` bits
3. Click **Generate**
4. You will see two boxes: **Public Key** and **Private Key**

- **Save your Private Key** somewhere
- **Do not share your Private Key**

### Step 2: Submit Your Public Key

Share **only** your Public Key

---

### Step 3: View Your Assignment

Visit:

**[https://monochromaticcoder.github.io/secret-santa/](https://monochromaticcoder.github.io/secret-santa/)**

Find your name in the table and **copy the encrypted assignment** (long hex string).

---

### Step 4: Decrypt Your Assignment

1. Visit https://emn178.github.io/online-tools/rsa/decrypt/
2. Set "Algorithm" to "ECB / OAEP / SHA1"
3. Paste your **Private Key** into the "Private Key" box
4. Paste the **encrypted assignment** (hex string) into the "Cipher Text" box
5. Click **Decrypt**

### Add Participants

Edit `config.py`:

```python
PARTICIPANTS = [
    Participant(
        id="Alice",
        public_key_pem="""-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----""",
        cannot_give_to={"Bob"}  # Restrictions
    ),
    # Add others...
]
```
