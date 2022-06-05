from dataclasses import dataclass


@dataclass
class FullyQualifiedCommand:
    context: str
    space_type: str
    region_type: str
    command: str
    options: dict = None

    def __str__(self):
        return (
            "{ "
            + f"'context': '{self.context}', "
            + f"'space_type': '{self.space_type}', "
            + f"'region_type': '{self.region_type}', "
            + f"'command': '{self.command}', "
            + f"'options': '{self.options}' "
            + "}"
        )


@dataclass(frozen=True)
class KeyCombo(dict):
    type: str
    value: str
    alt: bool
    shift: bool
    ctrl: bool
    oskey: bool

    @classmethod
    def from_dict(cls, obj):
        return KeyCombo(
            type=obj["type"],
            value=obj["value"],
            alt=obj.get("alt", False),
            shift=obj.get("shift", False),
            ctrl=obj.get("ctrl", False),
            oskey=obj.get("oskey", False),
        )

    @classmethod
    def from_str(cls, s):
        value, rest = s.split(" ")
        oskey = "cmd-" in rest
        alt = "option-" in rest
        shift = "shift-" in rest
        ctrl = "ctrl-" in rest
        type = (
            rest.replace("cmd-", "")
            .replace("option-", "")
            .replace("shift-", "")
            .replace("ctrl-", "")
        )
        return KeyCombo(
            value=value, oskey=oskey, alt=alt, shift=shift, ctrl=ctrl, type=type
        )

    def to_dict(self):
        return {
            "value": self.value,
            "type": self.type,
            "alt": self.alt,
            "oskey": self.oskey,
            "shift": self.shift,
            "ctrl": self.ctrl,
        }

    def __str__(self):
        s = self.value + " "
        if self.oskey:
            s += "cmd-"
        if self.alt:
            s += "option-"
        if self.shift:
            s += "shift-"
        if self.ctrl:
            s += "ctrl-"
        s += self.type
        return s


def get_context_names(entries):
    names = set()
    for entry in entries:
        commands = entry[1]
        for command in commands:
            names.add(command["context"])
    return names


def compile(entries):
    context_names = get_context_names(entries)
    output = []
    for context_name in context_names:
        context = [context_name]
        context_types = {}
        items = []
        for entry in entries:
            keycombo = KeyCombo.from_str(entry[0]).to_dict()
            for cmd in entry[1]:
                context_types["space_type"] = cmd["space_type"]
                context_types["region_type"] = cmd["region_type"]
                nextitem = (cmd["command"], keycombo, cmd["options"])
                items.append(nextitem)

        context.append(context_types)
        context.append({"items": items})
        output.append(tuple(context))
        print("keyconfig_version = (3, 1, 7)")
        print("keyconfig_data = ", output)
        return output


keyconfig_version = (3, 1, 7)
keyconfig_data = compile(
    [
        (
            "PRESS option-W",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "bc.tool_activate",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-W",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hardflow.topbar_activate",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-ctrl-L",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.adjust_logo",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ACCENT_GRAVE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.tilde_remap",
                    "options": "None",
                },
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.bevel_helper",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.bev_multi",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.bevel",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-X",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.mirror_gizmo",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-V",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.rip_move",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.stitch",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-ACCENT_GRAVE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.helper",
                    "options": "None",
                },
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-K",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hops.pref_helper",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_column",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS Q",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-Q",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-D",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "object.flow_cursor_dupl",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-X",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-X",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dissolve_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-V",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "object.paste_in_place",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.paste",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.paste",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-RIGHTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.cursor3d",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.cursor_set",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.change_frame",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.cursor_set",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.cursor_set",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.cursor_set",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.cursor_set",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY shift-EVT_TWEAK_R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_SLASH",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.localview",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS SLASH",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.localview",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY MOUSESMARTZOOM",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.localview",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.localview_remove_from",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "marker.add",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.add",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "object.move_to_collection",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "marker.add",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY MOUSEROTATE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.rotate",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.rotate",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_pan",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.move",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_pan",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY TRACKPADPAN",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.rotate",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_pan",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY shift-TRACKPADPAN",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.move",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_PERIOD",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_PERIOD",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_PERIOD",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_selected",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_selected",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.view_selected",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.show_active",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_selected",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY TIMER1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.smoothview",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY TRACKPADZOOM",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-TRACKPADPAN",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY ctrl-TRACKPADPAN",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_PLUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_in",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.show_one_level",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "ACCELERATE",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_out",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.show_one_level",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "DECELERATE",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-EQUAL",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-EQUAL",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS WHEELINMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_in",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS WHEELOUTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_out",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-NUMPAD_PLUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NUMPAD_MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-EQUAL",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-EQUAL",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-MINUS",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.dolly",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS HOME",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_center_camera",
                    "options": "None",
                },
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_center_lock",
                    "options": "None",
                },
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_all",
                    "options": "None",
                },
                {
                    "context": "Clip Dopesheet Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.dopesheet_view_all",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_view_all",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.view_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.show_hierarchy",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_all_preview",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-HOME",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_all",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-HOME",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_all",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-C",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_all",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ACCENT_GRAVE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.navigate",
                    "options": "None",
                },
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.navigate",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_0",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_camera",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_center_current_frame",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.view_frame",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_frame",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_2",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_orbit",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_4",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_orbit",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NUMPAD_5",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_persportho",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_6",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_orbit",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_8",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_orbit",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_2",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_2",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-NUMPAD_4",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_4",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-NUMPAD_6",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_6",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_8",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_8",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_pan",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-NUMPAD_4",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_roll",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-NUMPAD_6",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_roll",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_9",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_orbit",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-NUMPAD_1",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-NUMPAD_3",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-NUMPAD_7",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "NORTH option-EVT_TWEAK_M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "SOUTH option-EVT_TWEAK_M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "EAST option-EVT_TWEAK_M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "WEST option-EVT_TWEAK_M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "CLICK option-MIDDLEMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_center_pick",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_orbit_zoom",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_ndof",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_orbit",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY ctrl-NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_orbit",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY shift-NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_pan",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY cmd-shift-NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_all",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY shift-ctrl-NDOF_MOTION",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.ndof_all",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_FIT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_selected",
                    "options": "None",
                },
                {
                    "context": "Clip Dopesheet Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.dopesheet_view_all",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_view_all",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.view_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_all_preview",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS NDOF_BUTTON_ROLL_CW",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_roll",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_ROLL_CCW",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_roll",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_FRONT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_BACK",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_LEFT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_RIGHT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_TOP",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NDOF_BUTTON_BOTTOM",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NDOF_BUTTON_FRONT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NDOF_BUTTON_RIGHT",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NDOF_BUTTON_TOP",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.view_axis",
                    "options": "None",
                }
            ],
        ),
        (
            "CLICK LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_openclose",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK shift-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_openclose",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.shortest_path_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.shortest_path_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK ctrl-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.shortest_path_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.shortest_path_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK option-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.loop_select",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_loop",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-shift-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.shortest_path_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.shortest_path_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK shift-ctrl-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.shortest_path_pick",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_activate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.shortest_path_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-option-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.edgering_select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_edge_ring",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK option-ctrl-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.edgering_select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_edge_ring",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK option-shift-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.loop_select",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_loop",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-option-shift-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.edgering_select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_edge_ring",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK option-shift-ctrl-LEFTMOUSE",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.edgering_select",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_edge_ring",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_box",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_box",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_box",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_box",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_box",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_box",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.tool_set_by_id",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_box",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
                {
                    "context": "Spreadsheet Generic",
                    "space_type": "SPREADSHEET",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-EVT_TWEAK_R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_lasso",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY ctrl-EVT_TWEAK_R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_lasso",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-shift-EVT_TWEAK_R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_lasso",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY shift-ctrl-EVT_TWEAK_R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_lasso",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS C",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.select_circle",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_circle",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_circle",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_circle",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.collection_new",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_circle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.clip_border",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.zoom_border",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.render_border",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.camera_bind",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.bevel",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.render_border",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.camera_bind",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.bevel",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-option-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.clear_render_border",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-B",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.clear_render_border",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-option-NUMPAD_0",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.camera_to_view",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-NUMPAD_0",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.camera_to_view",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-NUMPAD_0",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.object_as_camera",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_0",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.object_as_camera",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-C",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.copybuffer",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.copy_tracks",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.copy",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.report_copy",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.copy_splines",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.id_copy",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.copy",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-C",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.copybuffer",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.copy_tracks",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.copy",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.report_copy",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.copy_splines",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.id_copy",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.copy",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-V",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.pastebuffer",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.paste_tracks",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.paste",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.paste_splines",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.id_paste",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.paste",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-V",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.pastebuffer",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.paste_tracks",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.paste",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.paste_splines",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.id_paste",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.paste",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY EVT_TWEAK_L",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "3D View Tool: Move",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_box",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.move",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_box",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_box",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_openclose",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_drag_drop",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.seq_slide",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS G",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.move",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.seq_slide",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.translate",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "GRAVITY_TOGGLE",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS R",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.report_replay",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.reassign_inputs",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.rotate",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS S",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.slip",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.resize",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-S",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.tosphere",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.save_as",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.tosphere",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-option-shift-S",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-ctrl-S",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.shear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-W",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.bend",
                    "options": "None",
                },
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-M",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.mirror",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.mirror",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "marker.rename",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.rename",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "marker.rename",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.mirror",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-T",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "object.transform_axis_target",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-A",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.skin_resize",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_apply",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.gpencil_modifier_apply",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "constraint.apply",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-A",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "transform.skin_resize",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_apply",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.gpencil_modifier_apply",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "constraint.apply",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-TAB",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "nla.tweakmode_enter",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "nla.tweakmode_exit",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-TAB",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_panel",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_menu_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-TAB",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_panel",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_menu_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-S",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.snap",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS PERIOD",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.show_active",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "UP",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS COMMA",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FORWARD",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS Z",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-Z",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.toggle_shading",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-Z",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "view3d.toggle_xray",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-Z",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS W",
            [
                {
                    "context": "3D View",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.tool_set_by_id",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.tool_set_by_id",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS OSKEY",
            [
                {
                    "context": "3D View Tool: Hardflow",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hardflow.display",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS RIGHT_CTRL",
            [
                {
                    "context": "3D View Tool: Hardflow",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hardflow_om.display",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS LEFT_CTRL",
            [
                {
                    "context": "3D View Tool: Hardflow",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "hardflow.display",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS E",
            [
                {
                    "context": "3D View Tool: Hardflow",
                    "space_type": "VIEW_3D",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.transform",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "view3d.edit_mesh_extrude_move_normal",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.collection_exclude_set",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "transform.transform",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "RIGHT",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS T",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.interpolation_type",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Node Generic",
                    "space_type": "NODE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS N",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Dopesheet Generic",
                    "space_type": "DOPESHEET_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Node Generic",
                    "space_type": "NODE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-O",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.open",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.smooth",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.open",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.offset_clear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-LEFT_ARROW",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.swap",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-RIGHT_ARROW",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.swap",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-T",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.quads_convert_to_tris",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-T",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.quads_convert_to_tris",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-T",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.quads_convert_to_tris",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-T",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.track_markers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.quads_convert_to_tris",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS TAB",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle_enum",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "anim.channels_editable_toggle",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "nla.tweakmode_enter",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "nla.tweakmode_exit",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.meta_toggle",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "GRAVITY_TOGGLE",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS P",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.prefetch",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.separate",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.pin",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-E",
            [
                {
                    "context": "Clip",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Dopesheet Generic",
                    "space_type": "DOPESHEET_EDITOR",
                    "region_type": "WINDOW",
                    "command": "action.extrapolation_type",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.edge_crease",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS LEFTMOUSE",
            [
                {
                    "context": "Clip Dopesheet Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.dopesheet_select_channel",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.change_frame",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select",
                    "options": "None",
                },
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.slide_marker",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.slide_point",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.slide_spline_curvature",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_set_active",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-NUMPAD_8",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-NUMPAD_2",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_zoom_ratio",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS F",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.view_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.edge_face_add",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-LEFT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-LEFT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-RIGHT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-RIGHT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-LEFT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-RIGHT_ARROW",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.frame_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-LEFTMOUSE",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS A",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_all_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_all",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_all",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_all",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_all",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "LEFT",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-A",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_all_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_all",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_all",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_all",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_all",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-I",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_all_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_all",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_all",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_all",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_all",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-I",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_all_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_all",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_all",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_all",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_all",
                    "options": "None",
                },
            ],
        ),
        (
            "DOUBLE_CLICK A",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_all",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_select_all_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_all",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.select_all",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select_all",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_all",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_all",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_all",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_all",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-G",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_grouped",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-option-EVT_TWEAK_R",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY option-ctrl-EVT_TWEAK_R",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-option-shift-EVT_TWEAK_R",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY option-shift-ctrl-EVT_TWEAK_R",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.select_lasso",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_lasso",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-LEFTMOUSE",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.add_marker_slide",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.add_vertex_slide",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "clip.select",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-LEFTMOUSE",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.add_marker_slide",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.add_vertex_slide",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "clip.select",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-X",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.delete_marker",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_delete_knot",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-DEL",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.delete_marker",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_delete_knot",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-D",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.disable_markers",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_disable_markers",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.duplicate_move",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.duplicate",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.duplicate_move",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.duplicate_move",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_copy",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.gpencil_modifier_copy",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.shaderfx_copy",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "constraint.copy",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.duplicate_move",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS X",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.delete_track",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_delete_curve",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.report_delete",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.delete",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.delete",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.delete",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.gpencil_modifier_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.shaderfx_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "constraint.delete",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.delete",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.delete",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS DEL",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.delete_track",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.graph_delete_curve",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.delete",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "info.report_delete",
                    "options": "None",
                },
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.delete",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.delete",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.delete",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.modifier_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.gpencil_modifier_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "object.shaderfx_remove",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "constraint.delete",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.delete",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.delete",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-L",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.lock_tracks",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_linked",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_linked",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_linked",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_linked",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-L",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.lock_tracks",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_linked",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_linked",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_linked",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_linked",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-L",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.lock_tracks",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.point_normals",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-H",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.hide_tracks_clear",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.hide_view_clear",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.reveal",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.unhide_all",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.unmute",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.reveal",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS H",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.hide_tracks",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.hide_view_set",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.hide",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.hide",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.mute",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.hide",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-H",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.hide_tracks",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.hide_view_set",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.hide",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.mute",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.hide",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK_DRAG LEFTMOUSE",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.slide_plane_marker",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS I",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.keyframe_insert",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.keyframe_insert",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.shape_key_insert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.inset",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "anim.keyframe_insert",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-I",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.keyframe_delete",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.shape_key_clear",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "anim.keyframe_delete",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-J",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.join_tracks",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-J",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.join_tracks",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS L",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.lock_selection_toggle",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_linked",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_linked_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-D",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.rip_edge_move",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-S",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.save",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.transform",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.shrink_fatten",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.swap_inputs",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_transform_clear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-T",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-T",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
                {
                    "context": "Clip Graph Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "clip.clear_track_path",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS RIGHTMOUSE",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.operation",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "buttons.context_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS APP",
            [
                {
                    "context": "Clip Editor",
                    "space_type": "CLIP_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Info",
                    "space_type": "INFO",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-TAB",
            [
                {
                    "context": "Dopesheet Generic",
                    "space_type": "DOPESHEET_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_enum",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS LEFT_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_offset",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "LEFT",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS RIGHT_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_offset",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "RIGHT",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-RIGHT_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_jump",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-LEFT_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_jump",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS UP_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.keyframe_jump",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FORWARD",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS DOWN_ARROW",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.keyframe_jump",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "BACKWARD",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS MEDIA_LAST",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.keyframe_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS MEDIA_FIRST",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.keyframe_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-WHEELDOWNMOUSE",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_offset",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-WHEELUPMOUSE",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.frame_offset",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-SPACE",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_play",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-SPACE",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_play",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-SPACE",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_play",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ESC",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_cancel",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "CANCEL",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS MEDIA_PLAY",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_play",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS MEDIA_STOP",
            [
                {
                    "context": "Frames",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "screen.animation_cancel",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-H",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.lock",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-option-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-option-shift-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-ctrl-LEFTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.clickselect",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS LEFT_BRACKET",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_side_of_frame",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS RIGHT_BRACKET",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_leftright",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_side_of_frame",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY shift-EVT_TWEAK_L",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_box",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_drag_drop",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY cmd-EVT_TWEAK_L",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_box",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY ctrl-EVT_TWEAK_L",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_box",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_box",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_box",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS K",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_column",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.knife_tool",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.keyingset_add_selected",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-K",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_column",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-K",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_column",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.knife_tool",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-K",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_column",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.keyingset_remove_selected",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-NUMPAD_PLUS",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_more",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_more",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_more",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_more",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_more",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_PLUS",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_more",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_more",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_more",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_more",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_more",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-NUMPAD_MINUS",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_less",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_less",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_less",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_less",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_less",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-NUMPAD_MINUS",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.select_less",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_less",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_less",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_less",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_less",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-G",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.frame_jump",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.meta_make",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-G",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.frame_jump",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.meta_make",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS V",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.handle_type",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.handle_type_set",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.rip_move",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.rip_move",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-E",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.easing_type",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.mark_seam",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-E",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.easing_type",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.mark_seam",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-O",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.sample",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-C",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.bake",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.cyclic_toggle",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-RIGHTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.click_insert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dupli_extrude_cursor",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK ctrl-RIGHTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.click_insert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dupli_extrude_cursor",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK cmd-shift-RIGHTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.click_insert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dupli_extrude_cursor",
                    "options": "None",
                },
            ],
        ),
        (
            "CLICK shift-ctrl-RIGHTMOUSE",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.click_insert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dupli_extrude_cursor",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-V",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.paste",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.paste",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-option-P",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.previewrange_set",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-P",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.previewrange_set",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-M",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.fmodifier_add",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mirror",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-M",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "graph.fmodifier_add",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mirror",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-O",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu_pie",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS O",
            [
                {
                    "context": "Graph Editor",
                    "space_type": "GRAPH_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_int",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.view_ghost_border",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "BACKWARD",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-N",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.new",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.new",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-R",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.reload",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.reload",
                    "options": "None",
                },
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_transform_clear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-R",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.read_viewlayers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.loopcut_slide",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-R",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.read_viewlayers",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.loopcut_slide",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS J",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.cycle_render_slot",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.vert_connect_path",
                    "options": "None",
                },
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "TELEPORT",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-J",
            [
                {
                    "context": "Image Generic",
                    "space_type": "IMAGE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "image.cycle_render_slot",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.tris_convert_to_quads",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-LEFTMOUSE",
            [
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.add_feather_vertex_slide",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-LEFTMOUSE",
            [
                {
                    "context": "Markers",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "marker.select",
                    "options": "None",
                },
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.add_feather_vertex_slide",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-A",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.expanded_toggle",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-L",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.select_linked_pick",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_linked_pick",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-N",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.normals_make_consistent",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.normals_make_consistent",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-P",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.parent_set",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "object.vertex_parent_set",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-P",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.parent_set",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "object.vertex_parent_set",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-P",
            [
                {
                    "context": "Mask Editing",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mask.parent_clear",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.pin",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-U",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "zenuv.call_popup",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "zenuv.call_popup",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-U",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "zenuv.call_pie",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "zenuv.call_pie",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.clean_up",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "machin3.collapse_outliner",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS FOUR",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_face",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "machin3.toggle_outliner_children",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_edge",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_edge",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_edge",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "machin3.expand_outliner",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-shift-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_vert",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_vert",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_vert",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_vert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "machin3.smart_vert",
                    "options": "None",
                },
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "machin3.toggle_outliner_group_mode",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.context_set_enum",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-ctrl-NUMPAD_MINUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "hops.edit_bool_difference",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-NUMPAD_PLUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "hops.edit_bool_union",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-R",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.offset_edge_loops_slide",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-R",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.offset_edge_loops_slide",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-B",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.bevel",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-ONE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-TWO",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-ctrl-THREE",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_mode",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-shift-NUMPAD_PLUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_next_item",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-NUMPAD_PLUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_next_item",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-NUMPAD_MINUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_prev_item",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-NUMPAD_MINUS",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.select_prev_item",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-shift-N",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.normals_make_consistent",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-ctrl-N",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.normals_make_consistent",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-E",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.collection_exclude_clear",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-F",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.fill",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "buttons.clear_filter",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS Y",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.split",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.images_separate",
                    "options": "None",
                },
                {
                    "context": "Spreadsheet Generic",
                    "space_type": "SPREADSHEET",
                    "region_type": "WINDOW",
                    "command": "wm.context_toggle",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_split",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS shift-V",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "transform.vert_slide",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-X",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dissolve_mode",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-DEL",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dissolve_mode",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-DEL",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "mesh.dissolve_mode",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-F",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "anim.channels_select_filter",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "buttons.start_filter",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS ctrl-F",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "NLA Generic",
                    "space_type": "NLA_EDITOR",
                    "region_type": "WINDOW",
                    "command": "anim.channels_select_filter",
                    "options": "None",
                },
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "buttons.start_filter",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS U",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "wm.call_menu",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-option-G",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "object.vertex_group_remove_from",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.meta_separate",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS option-ctrl-G",
            [
                {
                    "context": "Mesh",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "object.vertex_group_remove_from",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.meta_separate",
                    "options": "None",
                },
            ],
        ),
        (
            "ANY MOUSEMOVE",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.highlight_update",
                    "options": "None",
                }
            ],
        ),
        (
            "DOUBLE_CLICK LEFTMOUSE",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_rename",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS F2",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.item_rename",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-UP_ARROW",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-DOWN_ARROW",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.select_walk",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS PAGE_DOWN",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.scroll_page",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_jump",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS PAGE_UP",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.scroll_page",
                    "options": "None",
                },
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_jump",
                    "options": "None",
                },
            ],
        ),
        (
            "PRESS cmd-D",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.drivers_add_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-D",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.drivers_add_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-option-D",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.drivers_delete_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-D",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "outliner.drivers_delete_selected",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-M",
            [
                {
                    "context": "Outliner",
                    "space_type": "OUTLINER",
                    "region_type": "WINDOW",
                    "command": "object.link_to_collection",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-WHEELUPMOUSE",
            [
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "screen.space_context_cycle",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-WHEELUPMOUSE",
            [
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "screen.space_context_cycle",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-WHEELDOWNMOUSE",
            [
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "screen.space_context_cycle",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ctrl-WHEELDOWNMOUSE",
            [
                {
                    "context": "Property Editor",
                    "space_type": "PROPERTIES",
                    "region_type": "WINDOW",
                    "command": "screen.space_context_cycle",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-H",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.unmute",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS cmd-option-H",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.unlock",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-ctrl-H",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.unlock",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-shift-R",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.reload",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-PAGE_UP",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-PAGE_DOWN",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_jump",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS BACK_SPACE",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.gap_remove",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-BACK_SPACE",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.gap_remove",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-EQUAL",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.gap_insert",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS FIVE",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS SIX",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS SEVEN",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS EIGHT",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NINE",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS ZERO",
            [
                {
                    "context": "Sequencer",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.split_multicam",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS option-G",
            [
                {
                    "context": "SequencerPreview",
                    "space_type": "SEQUENCE_EDITOR",
                    "region_type": "WINDOW",
                    "command": "sequencer.strip_transform_clear",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS shift-P",
            [
                {
                    "context": "UV Editor",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "uv.select_pinned",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY RIGHTMOUSE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "CANCEL",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY LEFTMOUSE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "CONFIRM",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS RET",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "CONFIRM",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS NUMPAD_ENTER",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "CONFIRM",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS LEFT_SHIFT",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FAST_ENABLE",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE LEFT_SHIFT",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FAST_DISABLE",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS LEFT_ALT",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "SLOW_ENABLE",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE LEFT_ALT",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "SLOW_DISABLE",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS QUOTE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "DOWN",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE COMMA",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FORWARD_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE O",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "BACKWARD_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE A",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "LEFT_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE E",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "RIGHT_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE PERIOD",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "UP_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE QUOTE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "DOWN_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE UP_ARROW",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "FORWARD_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE DOWN_ARROW",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "BACKWARD_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE LEFT_ARROW",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "LEFT_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE RIGHT_ARROW",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "RIGHT_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS SPACE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "JUMP",
                    "options": "None",
                }
            ],
        ),
        (
            "RELEASE SPACE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "JUMP_STOP",
                    "options": "None",
                }
            ],
        ),
        (
            "ANY MIDDLEMOUSE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "TELEPORT",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS WHEELUPMOUSE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "ACCELERATE",
                    "options": "None",
                }
            ],
        ),
        (
            "PRESS WHEELDOWNMOUSE",
            [
                {
                    "context": "View3D Walk Modal",
                    "space_type": "EMPTY",
                    "region_type": "WINDOW",
                    "command": "DECELERATE",
                    "options": "None",
                }
            ],
        ),
    ]
)
