# IF4020_T4_CrackingRSA
### Section A: Weak RSA Parameters (Question.py)
#### How to run:
1. Run the `Question.py` to generate a test case
```sh
python3 Question.py
```

2. Run the `Cracker.py` in another terminal tab
```sh
python3 Cracker.py
```

3. Input the `n, e, c` from `Question.py` terminal to the `Cracker.py`'s terminal


### Section B: Vulnerabilities on Arsip.py
1. There is no input validation for user input especially for integer inputs so
we can use negative numbers to exploit and get access to the arsip array's index
2. We can generate an access token using the negative index of `nomor_arsip_admin` and when we're trying to read
the index we can make use of negative of the access token to access the real index of
`nomor_arsip_admin` proof is given in the pdf. Hence, we can crack the arsip[nomor_arsip_admin] info.
