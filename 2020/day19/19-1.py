rules, msgs = open("input.txt").read().split("\n\n")

rules = { line.split(":")[0]: line.split(": ")[1] for line in rules.split("\n") }

def match_grammar(s, rule_num):
  rule = rules[rule_num]
  if rule[0] == '"': # terminal rule
    rule = rule.strip('"')
    if s.startswith(rule):
      return len(rule)
    else:
      return -1

  for subrule in rule.split(" | "):
    counter = 0
    for num in subrule.split(" "):
      count_matches = match_grammar(s[counter:], num)
      if count_matches == -1:
        counter = -1
        break
      counter += count_matches

    if counter != -1: 
      return counter # can already return since it's an OR!

  return -1


matches = 0
for msg in msgs.split("\n"):
  matches += match_grammar(msg, "0") == len(msg)

print(matches)
