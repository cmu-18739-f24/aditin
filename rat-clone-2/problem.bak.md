# Guess My Cheese

- Namespace: picoctf
- ID: rat-clone-1
- Type: custom
- Category: General Skills
- Points: 1
- Templatable: no
- MaxUsers: 0
- ports:
  - name: socat
  - port: 5555
  - protocol: tcp

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`



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
