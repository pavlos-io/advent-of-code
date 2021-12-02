rules, msgs = open("input.txt").read().split("\n\n")

rules = { line.split(":")[0]: line.split(": ")[1] for line in rules.split("\n") }

rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"

def match_grammar(s, rule_num):
  rule = rules[rule_num]
  if rule[0] == '"': # terminal rule
    rule = rule.strip('"')
    if s.startswith(rule):
      return [len(rule)]
    else:
      return []

  out = []
  for subrule in rule.split(" | "):
    counter = [0]
    for num in subrule.split(" "):
      tmp = []
      for c in counter:
        count_matches = match_grammar(s[c:], num)
        for m in count_matches:
          tmp.append(m + c)
      counter = tmp
    out += counter

  return out


matches = 0
for msg in msgs.split("\n"):
  matches += len(msg) in match_grammar(msg, "0")

print(matches)
