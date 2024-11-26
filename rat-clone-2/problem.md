# Guess My Cheese (Part 2)

- Namespace: picoctf/18739f24
- ID: rat-clone-2
- Type: custom
- Category: Cryptography
- Points: 1
- Templatable: yes


## Description

The imposter was able to fool us last time, so we've strengthened our defenses!

## Details

Connect to the program on our server: `nc {{server}} {{port}}`

Download the program: {{url_for("challenge.py")}}


## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Attributes

- author: aditin
