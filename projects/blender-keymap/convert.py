import bindings
from compile import FullyQualifiedCommand, KeyCombo

allcommands = []
commandsmap = {}


def register_command(combo, cmd):
    if combo in commandsmap:
        commandsmap[combo].append(cmd)
    else:
        commandsmap[combo] = [cmd]


for context_group in bindings.keyconfig_data:
    context = context_group[0]
    types = context_group[1]
    specs = context_group[2]
    for item in specs["items"]:
        command = item[0]
        keycombo = KeyCombo.from_dict(item[1])
        options = item[2]
        fqcommand = FullyQualifiedCommand(
            context, types["space_type"], types["region_type"], command
        )
        allcommands.append(fqcommand)
        register_command(keycombo, fqcommand)

for k, v in commandsmap.items():
    print("('" + str(k) + "', [" + ", ".join([str(item) for item in v]) + "]" + "),")
