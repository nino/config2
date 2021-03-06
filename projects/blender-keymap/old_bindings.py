keyconfig_version = (3, 1, 7)
keyconfig_data = [
    (
        "3D View",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "bc.tool_activate",
                    {"type": "W", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "hardflow.topbar_activate",
                    {"type": "W", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                (
                    "hops.adjust_logo",
                    {
                        "type": "L",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "hops.tilde_remap",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "active": False,
                    },
                ),
                (
                    "hops.bevel_helper",
                    {"type": "B", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                (
                    "hops.bev_multi",
                    {"type": "B", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "hops.mirror_gizmo",
                    {"type": "X", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "V", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "HOPS_MT_ViewportSubmenu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "HOPS_MT_MaterialListMenu"),
                        ],
                    },
                ),
                (
                    "hops.helper",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "hops.pref_helper",
                    {"type": "K", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "Q", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "HOPS_MT_MainMenu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "Q", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "HOPS_MT_MainPie"),
                        ],
                    },
                ),
                (
                    "object.flow_cursor_dupl",
                    {"type": "D", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", "FLOW_MT_main_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "X", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "FLOW_MT_PieMenu"),
                        ],
                    },
                ),
                (
                    "object.paste_in_place",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "view3d.cursor3d",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
                ("view3d.localview", {"type": "NUMPAD_SLASH", "value": "PRESS"}, None),
                (
                    "view3d.localview",
                    {"type": "SLASH", "value": "PRESS"},
                    {
                        "properties": [
                            ("frame_selected", False),
                        ],
                    },
                ),
                ("view3d.localview", {"type": "MOUSESMARTZOOM", "value": "ANY"}, None),
                ("view3d.localview_remove_from", {"type": "M", "value": "PRESS"}, None),
                ("view3d.rotate", {"type": "MOUSEROTATE", "value": "ANY"}, None),
                ("view3d.rotate", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                (
                    "view3d.move",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("view3d.rotate", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                (
                    "view3d.move",
                    {"type": "TRACKPADPAN", "value": "ANY", "shift": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "MIDDLEMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "MIDDLEMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "view3d.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                        ],
                    },
                ),
                (
                    "view3d.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                        ],
                    },
                ),
                (
                    "view3d.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    },
                ),
                (
                    "view3d.smoothview",
                    {"type": "TIMER1", "value": "ANY", "any": True},
                    None,
                ),
                ("view3d.zoom", {"type": "TRACKPADZOOM", "value": "ANY"}, None),
                (
                    "view3d.zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "oskey": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "view3d.zoom",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "EQUAL", "value": "PRESS", "oskey": True, "repeat": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "EQUAL", "value": "PRESS", "ctrl": True, "repeat": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "MINUS", "value": "PRESS", "oskey": True, "repeat": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "MINUS", "value": "PRESS", "ctrl": True, "repeat": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELINMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.zoom",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "EQUAL",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "EQUAL",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "MINUS",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "view3d.dolly",
                    {
                        "type": "MINUS",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                ("view3d.view_center_camera", {"type": "HOME", "value": "PRESS"}, None),
                ("view3d.view_center_lock", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "view3d.view_all",
                    {"type": "HOME", "value": "PRESS"},
                    {
                        "properties": [
                            ("center", False),
                        ],
                    },
                ),
                (
                    "view3d.view_all",
                    {"type": "HOME", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "view3d.view_all",
                    {"type": "HOME", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_all_regions", True),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "view3d.view_all",
                    {"type": "C", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("center", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_view_pie"),
                        ],
                    },
                ),
                (
                    "view3d.navigate",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "view3d.navigate",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("view3d.view_camera", {"type": "NUMPAD_0", "value": "PRESS"}, None),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FRONT"),
                        ],
                    },
                ),
                (
                    "view3d.view_orbit",
                    {"type": "NUMPAD_2", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("type", "ORBITDOWN"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_3", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_orbit",
                    {"type": "NUMPAD_4", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("type", "ORBITLEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_persportho",
                    {"type": "NUMPAD_5", "value": "PRESS"},
                    None,
                ),
                (
                    "view3d.view_orbit",
                    {"type": "NUMPAD_6", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("type", "ORBITRIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_7", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "TOP"),
                        ],
                    },
                ),
                (
                    "view3d.view_orbit",
                    {"type": "NUMPAD_8", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("type", "ORBITUP"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_1", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("type", "BACK"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_1", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "BACK"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_3", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_3", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_7", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_7", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_2",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANDOWN"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_2",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANDOWN"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_4",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANLEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_4",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANLEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_6",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANRIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_6",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANRIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_8",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANUP"),
                        ],
                    },
                ),
                (
                    "view3d.view_pan",
                    {
                        "type": "NUMPAD_8",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "PANUP"),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {
                        "type": "NUMPAD_4",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {
                        "type": "NUMPAD_6",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_orbit",
                    {"type": "NUMPAD_9", "value": "PRESS"},
                    {
                        "properties": [
                            ("angle", 3.1415927),
                            ("type", "ORBITRIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_1", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "FRONT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_3", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_7", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "TOP"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {
                        "type": "NUMPAD_1",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("type", "BACK"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_1", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "BACK"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {
                        "type": "NUMPAD_3",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("type", "LEFT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_3", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "LEFT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {
                        "type": "NUMPAD_7",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NUMPAD_7", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "EVT_TWEAK_M", "value": "NORTH", "alt": True},
                    {
                        "properties": [
                            ("type", "TOP"),
                            ("relative", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "EVT_TWEAK_M", "value": "SOUTH", "alt": True},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                            ("relative", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "EVT_TWEAK_M", "value": "EAST", "alt": True},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                            ("relative", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "EVT_TWEAK_M", "value": "WEST", "alt": True},
                    {
                        "properties": [
                            ("type", "LEFT"),
                            ("relative", True),
                        ],
                    },
                ),
                (
                    "view3d.view_center_pick",
                    {"type": "MIDDLEMOUSE", "value": "CLICK", "alt": True},
                    None,
                ),
                (
                    "view3d.ndof_orbit_zoom",
                    {"type": "NDOF_MOTION", "value": "ANY"},
                    None,
                ),
                (
                    "view3d.ndof_orbit",
                    {"type": "NDOF_MOTION", "value": "ANY", "oskey": True},
                    None,
                ),
                (
                    "view3d.ndof_orbit",
                    {"type": "NDOF_MOTION", "value": "ANY", "ctrl": True},
                    None,
                ),
                (
                    "view3d.ndof_pan",
                    {"type": "NDOF_MOTION", "value": "ANY", "shift": True},
                    None,
                ),
                (
                    "view3d.ndof_all",
                    {
                        "type": "NDOF_MOTION",
                        "value": "ANY",
                        "shift": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "view3d.ndof_all",
                    {
                        "type": "NDOF_MOTION",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                (
                    "view3d.view_selected",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_all_regions", False),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {"type": "NDOF_BUTTON_ROLL_CW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_roll",
                    {"type": "NDOF_BUTTON_ROLL_CCW", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_FRONT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FRONT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_BACK", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "BACK"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_LEFT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "LEFT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_RIGHT", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_TOP", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "TOP"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_BOTTOM", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "BOTTOM"),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_FRONT", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "FRONT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_RIGHT", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "RIGHT"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.view_axis",
                    {"type": "NDOF_BUTTON_TOP", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "TOP"),
                            ("align_active", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("center", True),
                            ("object", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("center", True),
                            ("object", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    {
                        "properties": [
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True, "oskey": True},
                    {
                        "properties": [
                            ("center", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("center", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("toggle", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                (
                    "view3d.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                            ("enumerate", True),
                        ],
                    },
                ),
                ("view3d.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "view3d.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "view3d.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                ("view3d.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "view3d.clip_border",
                    {"type": "B", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "view3d.zoom_border",
                    {"type": "B", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "view3d.render_border",
                    {"type": "B", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "view3d.render_border",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.clear_render_border",
                    {"type": "B", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "view3d.clear_render_border",
                    {"type": "B", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "view3d.camera_to_view",
                    {"type": "NUMPAD_0", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "view3d.camera_to_view",
                    {"type": "NUMPAD_0", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "view3d.object_as_camera",
                    {"type": "NUMPAD_0", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "view3d.object_as_camera",
                    {"type": "NUMPAD_0", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.copybuffer",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "view3d.copybuffer",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "view3d.pastebuffer",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "view3d.pastebuffer",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "transform.tosphere",
                    {"type": "S", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "transform.bend",
                    {"type": "W", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.mirror",
                    {"type": "M", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "object.transform_axis_target",
                    {"type": "T", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.skin_resize",
                    {"type": "A", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "transform.skin_resize",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap"),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "TAB", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_snapping"),
                            ("keep_open", True),
                        ],
                    },
                ),
                (
                    "wm.call_panel",
                    {"type": "TAB", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_PT_snapping"),
                            ("keep_open", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_snap_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_gizmo"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "COMMA", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_orientations_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "Z", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_shading_pie"),
                        ],
                    },
                ),
                (
                    "view3d.toggle_shading",
                    {"type": "Z", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "WIREFRAME"),
                        ],
                    },
                ),
                (
                    "view3d.toggle_xray",
                    {"type": "Z", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "Z", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.overlay.show_overlays"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Hardflow",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                ("hardflow.display", {"type": "OSKEY", "value": "PRESS"}, None),
                ("hardflow_om.display", {"type": "RIGHT_CTRL", "value": "PRESS"}, None),
                ("hardflow.display", {"type": "LEFT_CTRL", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "Hardflow_MT_pie"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "3D View Tool: Move",
        {"space_type": "VIEW_3D", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "key_modifier": "M"},
                    {
                        "properties": [
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Clip",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                ("clip.open", {"type": "O", "value": "PRESS", "alt": True}, None),
                (
                    "clip.track_markers",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", False),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", False),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("backwards", False),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "clip.track_markers",
                    {"type": "T", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("backwards", True),
                            ("sequence", True),
                        ],
                    },
                ),
                (
                    "wm.context_toggle_enum",
                    {"type": "TAB", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.mode"),
                            ("value_1", "TRACKING"),
                            ("value_2", "MASK"),
                        ],
                    },
                ),
                ("clip.prefetch", {"type": "P", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_solving_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "E", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_marker_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_reconstruction_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_view_pie"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Clip Dopesheet Editor",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "clip.dopesheet_select_channel",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                ("clip.dopesheet_view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "clip.dopesheet_view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
            ],
        },
    ),
    (
        "Clip Editor",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                ("clip.view_pan", {"type": "MIDDLEMOUSE", "value": "PRESS"}, None),
                (
                    "clip.view_pan",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.view_pan", {"type": "TRACKPADPAN", "value": "ANY"}, None),
                (
                    "clip.view_zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.view_zoom",
                    {"type": "MIDDLEMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("clip.view_zoom", {"type": "TRACKPADZOOM", "value": "ANY"}, None),
                (
                    "clip.view_zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "oskey": True},
                    None,
                ),
                (
                    "clip.view_zoom",
                    {"type": "TRACKPADPAN", "value": "ANY", "ctrl": True},
                    None,
                ),
                ("clip.view_zoom_in", {"type": "WHEELINMOUSE", "value": "PRESS"}, None),
                (
                    "clip.view_zoom_out",
                    {"type": "WHEELOUTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "clip.view_zoom_in",
                    {"type": "NUMPAD_PLUS", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "clip.view_zoom_out",
                    {"type": "NUMPAD_MINUS", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                    },
                ),
                (
                    "clip.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                    },
                ),
                ("clip.view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "clip.view_all",
                    {"type": "F", "value": "PRESS"},
                    {
                        "properties": [
                            ("fit_view", True),
                        ],
                    },
                ),
                (
                    "clip.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                ("clip.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                ("clip.view_ndof", {"type": "NDOF_MOTION", "value": "ANY"}, None),
                (
                    "clip.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHSTART"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHSTART"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHEND"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHEND"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "FAILEDPREV"),
                        ],
                    },
                ),
                (
                    "clip.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("position", "PATHSTART"),
                        ],
                    },
                ),
                ("clip.change_frame", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("clip.select_box", {"type": "B", "value": "PRESS"}, None),
                ("clip.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "CLIP_MT_select_grouped"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "alt": True, "oskey": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "clip.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "clip.add_marker_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.add_marker_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "clip.delete_marker",
                    {"type": "X", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "clip.delete_marker",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.slide_marker", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "clip.disable_markers",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "TOGGLE"),
                        ],
                    },
                ),
                ("clip.delete_track", {"type": "X", "value": "PRESS"}, None),
                ("clip.delete_track", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "clip.lock_tracks",
                    {"type": "L", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "LOCK"),
                        ],
                    },
                ),
                (
                    "clip.lock_tracks",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "LOCK"),
                        ],
                    },
                ),
                (
                    "clip.lock_tracks",
                    {"type": "L", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "UNLOCK"),
                        ],
                    },
                ),
                (
                    "clip.hide_tracks_clear",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "clip.hide_tracks",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "clip.hide_tracks",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "clip.slide_plane_marker",
                    {"type": "LEFTMOUSE", "value": "CLICK_DRAG"},
                    None,
                ),
                ("clip.keyframe_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "clip.keyframe_delete",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "clip.join_tracks",
                    {"type": "J", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.join_tracks",
                    {"type": "J", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("clip.lock_selection_toggle", {"type": "L", "value": "PRESS"}, None),
                (
                    "wm.context_toggle",
                    {"type": "D", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_disabled"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_marker_search"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.use_mute_footage"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "REMAINED"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "UPTO"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", "ALL"),
                            ("clear_active", False),
                        ],
                    },
                ),
                (
                    "clip.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "clip.copy_tracks",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.copy_tracks",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "clip.paste_tracks",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.paste_tracks",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_tracking_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "CLIP_MT_pivot_pie"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Clip Graph Editor",
        {"space_type": "CLIP_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                ("clip.graph_select", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "clip.graph_select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "clip.graph_select_all_markers",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("clip.graph_select_box", {"type": "B", "value": "PRESS"}, None),
                ("clip.graph_delete_curve", {"type": "X", "value": "PRESS"}, None),
                ("clip.graph_delete_curve", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "clip.graph_delete_knot",
                    {"type": "X", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "clip.graph_delete_knot",
                    {"type": "DEL", "value": "PRESS", "shift": True},
                    None,
                ),
                ("clip.graph_view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "clip.graph_view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                (
                    "clip.graph_center_current_frame",
                    {"type": "NUMPAD_0", "value": "PRESS"},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.lock_time_cursor"),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "REMAINED"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "UPTO"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.clear_track_path",
                    {"type": "T", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("action", "ALL"),
                            ("clear_active", True),
                        ],
                    },
                ),
                (
                    "clip.graph_disable_markers",
                    {"type": "D", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("action", "TOGGLE"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                (
                    "clip.change_frame",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Dopesheet Generic",
        {"space_type": "DOPESHEET_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "area.type"),
                            ("value", "GRAPH_EDITOR"),
                        ],
                    },
                ),
                (
                    "action.extrapolation_type",
                    {"type": "E", "value": "PRESS", "shift": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Frames",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "screen.frame_offset",
                    {"type": "LEFT_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("end", True),
                        ],
                    },
                ),
                (
                    "screen.frame_jump",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("end", False),
                        ],
                    },
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "UP_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("next", True),
                        ],
                    },
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "DOWN_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("next", False),
                        ],
                    },
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "MEDIA_LAST", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", True),
                        ],
                    },
                ),
                (
                    "screen.keyframe_jump",
                    {"type": "MEDIA_FIRST", "value": "PRESS"},
                    {
                        "properties": [
                            ("next", False),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", 1),
                        ],
                    },
                ),
                (
                    "screen.frame_offset",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("delta", -1),
                        ],
                    },
                ),
                (
                    "screen.animation_play",
                    {"type": "SPACE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "screen.animation_play",
                    {"type": "SPACE", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "screen.animation_play",
                    {"type": "SPACE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    },
                ),
                ("screen.animation_cancel", {"type": "ESC", "value": "PRESS"}, None),
                (
                    "screen.animation_play",
                    {"type": "MEDIA_PLAY", "value": "PRESS"},
                    None,
                ),
                (
                    "screen.animation_cancel",
                    {"type": "MEDIA_STOP", "value": "PRESS"},
                    None,
                ),
            ],
        },
    ),
    (
        "Graph Editor",
        {"space_type": "GRAPH_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_handles"),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("column", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("column", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "alt": True, "oskey": True},
                    {
                        "properties": [
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.clickselect",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("curves", True),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("mode", "CHECK"),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "CHECK"),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "CHECK"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "LEFT"),
                        ],
                    },
                ),
                (
                    "graph.select_leftright",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "RIGHT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "graph.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("graph.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "graph.select_box",
                    {"type": "B", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("axis_range", True),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SET"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "graph.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "graph.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "graph.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "graph.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "graph.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                ("graph.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "graph.select_column",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "KEYS"),
                        ],
                    },
                ),
                (
                    "graph.select_column",
                    {"type": "K", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("mode", "CFRA"),
                        ],
                    },
                ),
                (
                    "graph.select_column",
                    {"type": "K", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "CFRA"),
                        ],
                    },
                ),
                (
                    "graph.select_column",
                    {"type": "K", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "MARKERS_COLUMN"),
                        ],
                    },
                ),
                (
                    "graph.select_column",
                    {"type": "K", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "MARKERS_BETWEEN"),
                        ],
                    },
                ),
                (
                    "graph.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "graph.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "graph.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "graph.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                ("graph.select_linked", {"type": "L", "value": "PRESS"}, None),
                (
                    "graph.frame_jump",
                    {"type": "G", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "graph.frame_jump",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_snap_pie"),
                        ],
                    },
                ),
                ("graph.mirror", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                ("graph.handle_type", {"type": "V", "value": "PRESS"}, None),
                ("graph.interpolation_type", {"type": "T", "value": "PRESS"}, None),
                (
                    "graph.easing_type",
                    {"type": "E", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "graph.easing_type",
                    {"type": "E", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("graph.smooth", {"type": "O", "value": "PRESS", "alt": True}, None),
                (
                    "graph.sample",
                    {"type": "O", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                ("graph.bake", {"type": "C", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_delete"),
                        ],
                    },
                ),
                (
                    "graph.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("confirm", False),
                        ],
                    },
                ),
                (
                    "graph.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                ("graph.keyframe_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "graph.click_insert",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "oskey": True},
                    None,
                ),
                (
                    "graph.click_insert",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "ctrl": True},
                    None,
                ),
                (
                    "graph.click_insert",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "graph.click_insert",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                ("graph.copy", {"type": "C", "value": "PRESS", "oskey": True}, None),
                ("graph.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                ("graph.paste", {"type": "V", "value": "PRESS", "oskey": True}, None),
                ("graph.paste", {"type": "V", "value": "PRESS", "ctrl": True}, None),
                (
                    "graph.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    },
                ),
                (
                    "graph.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("flipped", True),
                        ],
                    },
                ),
                (
                    "graph.previewrange_set",
                    {"type": "P", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "graph.previewrange_set",
                    {"type": "P", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("graph.view_all", {"type": "HOME", "value": "PRESS"}, None),
                ("graph.view_all", {"type": "NDOF_BUTTON_FIT", "value": "PRESS"}, None),
                (
                    "graph.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                ("graph.view_frame", {"type": "NUMPAD_0", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_view_pie"),
                        ],
                    },
                ),
                (
                    "graph.fmodifier_add",
                    {"type": "M", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("only_active", False),
                        ],
                    },
                ),
                (
                    "graph.fmodifier_add",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("only_active", False),
                        ],
                    },
                ),
                (
                    "anim.channels_editable_toggle",
                    {"type": "TAB", "value": "PRESS"},
                    None,
                ),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "transform.transform",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_fcurve"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "GRAPH_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "graph.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Image Generic",
        {"space_type": "IMAGE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                ("image.new", {"type": "N", "value": "PRESS", "alt": True}, None),
                ("image.open", {"type": "O", "value": "PRESS", "alt": True}, None),
                ("image.reload", {"type": "R", "value": "PRESS", "alt": True}, None),
                (
                    "image.read_viewlayers",
                    {"type": "R", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "image.read_viewlayers",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("image.save", {"type": "S", "value": "PRESS", "alt": True}, None),
                (
                    "image.cycle_render_slot",
                    {"type": "J", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "image.cycle_render_slot",
                    {"type": "J", "value": "PRESS", "alt": True, "repeat": True},
                    {
                        "properties": [
                            ("reverse", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_view_pie"),
                        ],
                    },
                ),
                (
                    "image.save_as",
                    {"type": "S", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Info",
        {"space_type": "INFO", "region_type": "WINDOW"},
        {
            "items": [
                ("info.select_pick", {"type": "LEFTMOUSE", "value": "CLICK"}, None),
                (
                    "info.select_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "info.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("wait_for_input", False),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "info.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("info.select_box", {"type": "B", "value": "PRESS"}, None),
                ("info.report_replay", {"type": "R", "value": "PRESS"}, None),
                ("info.report_delete", {"type": "X", "value": "PRESS"}, None),
                ("info.report_delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "info.report_copy",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "info.report_copy",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "INFO_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "INFO_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Markers",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                (
                    "marker.move",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "marker.duplicate",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                ("marker.select", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "marker.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("camera", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("camera", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("camera", True),
                        ],
                    },
                ),
                (
                    "marker.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("camera", True),
                        ],
                    },
                ),
                (
                    "marker.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    },
                ),
                ("marker.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "marker.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "marker.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("marker.delete", {"type": "X", "value": "PRESS"}, None),
                ("marker.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("marker.rename", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                ("marker.move", {"type": "G", "value": "PRESS"}, None),
                (
                    "marker.camera_bind",
                    {"type": "B", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "marker.camera_bind",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Mask Editing",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                ("mask.new", {"type": "N", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "MASK_MT_add"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit_mask"),
                        ],
                    },
                ),
                (
                    "mask.add_vertex_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mask.add_vertex_slide",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.add_feather_vertex_slide",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "mask.add_feather_vertex_slide",
                    {
                        "type": "LEFTMOUSE",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                    },
                    None,
                ),
                ("mask.delete", {"type": "X", "value": "PRESS"}, None),
                ("mask.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "mask.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "mask.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mask.select_linked",
                    {"type": "L", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mask.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "mask.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                ("mask.select_box", {"type": "B", "value": "PRESS"}, None),
                ("mask.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "mask.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "alt": True, "oskey": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "mask.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "mask.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "mask.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "mask.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mask.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mask.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mask.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mask.hide_view_clear",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mask.hide_view_set",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "mask.hide_view_set",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "clip.select",
                    {"type": "LEFTMOUSE", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.cyclic_toggle",
                    {"type": "C", "value": "PRESS", "alt": True},
                    None,
                ),
                ("mask.slide_point", {"type": "LEFTMOUSE", "value": "PRESS"}, None),
                (
                    "mask.slide_spline_curvature",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                ("mask.handle_type_set", {"type": "V", "value": "PRESS"}, None),
                (
                    "mask.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "mask.parent_set",
                    {"type": "P", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mask.parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.parent_clear",
                    {"type": "P", "value": "PRESS", "alt": True},
                    None,
                ),
                ("mask.shape_key_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "mask.shape_key_clear",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mask.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "mask.copy_splines",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mask.copy_splines",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mask.paste_splines",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mask.paste_splines",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "transform.tosphere",
                    {"type": "S", "value": "PRESS", "shift": True, "alt": True},
                    None,
                ),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "transform.transform",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "MASK_SHRINKFATTEN"),
                        ],
                    },
                ),
                (
                    "uv.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Mesh",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.call_menu_pie",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "PIE_MT_selectionsem"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "PIE_MT_proportional_edt"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "PIE_MT_delete"),
                        ],
                    },
                ),
                (
                    "zenuv.call_popup",
                    {"type": "U", "value": "PRESS", "shift": True},
                    None,
                ),
                ("zenuv.call_pie", {"type": "U", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "MACHIN3_MT_align_pie"),
                        ],
                    },
                ),
                ("machin3.clean_up", {"type": "THREE", "value": "PRESS"}, None),
                ("machin3.smart_face", {"type": "FOUR", "value": "PRESS"}, None),
                (
                    "machin3.smart_edge",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("sharp", False),
                            ("offset", True),
                        ],
                    },
                ),
                (
                    "machin3.smart_edge",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("sharp", True),
                            ("offset", False),
                        ],
                    },
                ),
                (
                    "machin3.smart_edge",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("sharp", False),
                            ("offset", False),
                        ],
                    },
                ),
                (
                    "machin3.smart_vert",
                    {"type": "ONE", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("slideoverride", True),
                        ],
                    },
                ),
                (
                    "machin3.smart_vert",
                    {"type": "ONE", "value": "PRESS", "ctrl": True, "alt": True},
                    {
                        "properties": [
                            ("mode", "CONNECT"),
                            ("slideoverride", False),
                        ],
                    },
                ),
                (
                    "machin3.smart_vert",
                    {"type": "ONE", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("mode", "MERGE"),
                            ("mergetype", "PATHS"),
                            ("slideoverride", False),
                        ],
                    },
                ),
                (
                    "machin3.smart_vert",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("mode", "MERGE"),
                            ("mergetype", "CENTER"),
                            ("slideoverride", False),
                        ],
                    },
                ),
                (
                    "machin3.smart_vert",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "MERGE"),
                            ("mergetype", "LAST"),
                            ("slideoverride", False),
                        ],
                    },
                ),
                (
                    "hops.edit_bool_difference",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "hops.edit_bool_union",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "mesh.loopcut_slide",
                    {"type": "R", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            (
                                "TRANSFORM_OT_edge_slide",
                                [
                                    ("release_confirm", False),
                                ],
                            ),
                        ],
                    },
                ),
                (
                    "mesh.loopcut_slide",
                    {"type": "R", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            (
                                "TRANSFORM_OT_edge_slide",
                                [
                                    ("release_confirm", False),
                                ],
                            ),
                        ],
                    },
                ),
                (
                    "mesh.offset_edge_loops_slide",
                    {"type": "R", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            (
                                "TRANSFORM_OT_edge_slide",
                                [
                                    ("release_confirm", False),
                                ],
                            ),
                        ],
                    },
                ),
                (
                    "mesh.offset_edge_loops_slide",
                    {"type": "R", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            (
                                "TRANSFORM_OT_edge_slide",
                                [
                                    ("release_confirm", False),
                                ],
                            ),
                        ],
                    },
                ),
                ("mesh.inset", {"type": "I", "value": "PRESS"}, None),
                (
                    "mesh.bevel",
                    {"type": "B", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("affect", "EDGES"),
                        ],
                    },
                ),
                (
                    "mesh.bevel",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("affect", "EDGES"),
                        ],
                    },
                ),
                (
                    "transform.shrink_fatten",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mesh.bevel",
                    {"type": "B", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("affect", "VERTICES"),
                        ],
                    },
                ),
                (
                    "mesh.bevel",
                    {"type": "B", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("affect", "VERTICES"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    None,
                ),
                (
                    "mesh.loop_select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "mesh.edgering_select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "mesh.edgering_select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "mesh.edgering_select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "mesh.edgering_select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "mesh.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    },
                ),
                (
                    "mesh.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    },
                ),
                (
                    "mesh.shortest_path_pick",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("use_fill", True),
                        ],
                    },
                ),
                (
                    "mesh.shortest_path_pick",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("use_fill", True),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "mesh.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_next_item",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_next_item",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_prev_item",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "shift": True,
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_prev_item",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "mesh.select_linked",
                    {"type": "L", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mesh.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mesh.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "mesh.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "mesh.select_mirror",
                    {"type": "M", "value": "PRESS", "shift": True, "oskey": True},
                    None,
                ),
                (
                    "mesh.select_mirror",
                    {"type": "M", "value": "PRESS", "shift": True, "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_select_similar"),
                        ],
                    },
                ),
                ("mesh.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "mesh.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "mesh.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "mesh.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("inside", False),
                        ],
                    },
                ),
                (
                    "mesh.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("inside", True),
                        ],
                    },
                ),
                (
                    "mesh.normals_make_consistent",
                    {"type": "N", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("inside", True),
                        ],
                    },
                ),
                (
                    "view3d.edit_mesh_extrude_move_normal",
                    {"type": "E", "value": "PRESS"},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "E", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_extrude"),
                        ],
                    },
                ),
                (
                    "transform.edge_crease",
                    {"type": "E", "value": "PRESS", "shift": True},
                    None,
                ),
                ("mesh.fill", {"type": "F", "value": "PRESS", "alt": True}, None),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": "T", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("quad_method", "BEAUTY"),
                            ("ngon_method", "BEAUTY"),
                        ],
                    },
                ),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": "T", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("quad_method", "BEAUTY"),
                            ("ngon_method", "BEAUTY"),
                        ],
                    },
                ),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": "T", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("quad_method", "FIXED"),
                            ("ngon_method", "CLIP"),
                        ],
                    },
                ),
                (
                    "mesh.quads_convert_to_tris",
                    {"type": "T", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("quad_method", "FIXED"),
                            ("ngon_method", "CLIP"),
                        ],
                    },
                ),
                (
                    "mesh.tris_convert_to_quads",
                    {"type": "J", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "mesh.rip_move",
                    {"type": "V", "value": "PRESS"},
                    {
                        "properties": [
                            (
                                "MESH_OT_rip",
                                [
                                    ("use_fill", False),
                                ],
                            ),
                        ],
                    },
                ),
                (
                    "mesh.rip_move",
                    {"type": "V", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            (
                                "MESH_OT_rip",
                                [
                                    ("use_fill", True),
                                ],
                            ),
                        ],
                    },
                ),
                (
                    "mesh.rip_edge_move",
                    {"type": "D", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_merge"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_split"),
                        ],
                    },
                ),
                (
                    "mesh.edge_face_add",
                    {"type": "F", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "mesh.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_mesh_add"),
                        ],
                    },
                ),
                ("mesh.separate", {"type": "P", "value": "PRESS"}, None),
                ("mesh.split", {"type": "Y", "value": "PRESS"}, None),
                ("mesh.vert_connect_path", {"type": "J", "value": "PRESS"}, None),
                (
                    "mesh.point_normals",
                    {"type": "L", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "transform.vert_slide",
                    {"type": "V", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "mesh.dupli_extrude_cursor",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("rotate_source", True),
                        ],
                    },
                ),
                (
                    "mesh.dupli_extrude_cursor",
                    {"type": "RIGHTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("rotate_source", True),
                        ],
                    },
                ),
                (
                    "mesh.dupli_extrude_cursor",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("rotate_source", False),
                        ],
                    },
                ),
                (
                    "mesh.dupli_extrude_cursor",
                    {
                        "type": "RIGHTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("rotate_source", False),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_delete"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_delete"),
                        ],
                    },
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "X", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "X", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "DEL", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "mesh.dissolve_mode",
                    {"type": "DEL", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "mesh.knife_tool",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_occlude_geometry", True),
                            ("only_selected", False),
                        ],
                    },
                ),
                (
                    "mesh.knife_tool",
                    {"type": "K", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_occlude_geometry", False),
                            ("only_selected", True),
                        ],
                    },
                ),
                (
                    "object.vertex_parent_set",
                    {"type": "P", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "object.vertex_parent_set",
                    {"type": "P", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "F", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_faces"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_faces"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "E", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_edges"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "E", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_edges"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_vertices"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_vertices"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "H", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_hook"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_uv_map"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_vertex_group"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_vertex_group"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "N", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_normals"),
                        ],
                    },
                ),
                (
                    "object.vertex_group_remove_from",
                    {"type": "G", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "object.vertex_group_remove_from",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_connected"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_edit_mesh_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "B", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("name", "builtin.extrude_region"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "NLA Generic",
        {"space_type": "NLA_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                ("nla.tweakmode_enter", {"type": "TAB", "value": "PRESS"}, None),
                ("nla.tweakmode_exit", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "nla.tweakmode_enter",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("isolate_action", True),
                        ],
                    },
                ),
                (
                    "nla.tweakmode_exit",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("isolate_action", True),
                        ],
                    },
                ),
                (
                    "anim.channels_select_filter",
                    {"type": "F", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "anim.channels_select_filter",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Node Generic",
        {"space_type": "NODE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "T", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_toolbar"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "N", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Outliner",
        {"space_type": "OUTLINER", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "machin3.toggle_outliner_children",
                    {"type": "FOUR", "value": "PRESS"},
                    None,
                ),
                (
                    "machin3.collapse_outliner",
                    {"type": "THREE", "value": "PRESS"},
                    None,
                ),
                ("machin3.expand_outliner", {"type": "TWO", "value": "PRESS"}, None),
                (
                    "machin3.toggle_outliner_group_mode",
                    {"type": "ONE", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.highlight_update",
                    {"type": "MOUSEMOVE", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "outliner.item_rename",
                    {"type": "LEFTMOUSE", "value": "DOUBLE_CLICK"},
                    None,
                ),
                (
                    "outliner.item_rename",
                    {"type": "F2", "value": "PRESS"},
                    {
                        "properties": [
                            ("use_active", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend_range", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("extend_range", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_activate",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("extend_range", True),
                            ("deselect_all", True),
                        ],
                    },
                ),
                ("outliner.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "outliner.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("tweak", True),
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "UP_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("direction", "UP"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {
                        "type": "UP_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("direction", "UP"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "DOWN_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("direction", "DOWN"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {
                        "type": "DOWN_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("direction", "DOWN"),
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "LEFT_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("direction", "LEFT"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("direction", "LEFT"),
                            ("toggle_all", True),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                        ],
                    },
                ),
                (
                    "outliner.select_walk",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "shift": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("direction", "RIGHT"),
                            ("toggle_all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    },
                ),
                (
                    "outliner.item_openclose",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                ("outliner.operation", {"type": "RIGHTMOUSE", "value": "PRESS"}, None),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "OUTLINER_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "OUTLINER_MT_view_pie"),
                        ],
                    },
                ),
                (
                    "outliner.item_drag_drop",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    None,
                ),
                (
                    "outliner.item_drag_drop",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    None,
                ),
                ("outliner.show_hierarchy", {"type": "HOME", "value": "PRESS"}, None),
                ("outliner.show_active", {"type": "PERIOD", "value": "PRESS"}, None),
                (
                    "outliner.show_active",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.scroll_page",
                    {"type": "PAGE_DOWN", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("up", False),
                        ],
                    },
                ),
                (
                    "outliner.scroll_page",
                    {"type": "PAGE_UP", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("up", True),
                        ],
                    },
                ),
                (
                    "outliner.show_one_level",
                    {"type": "NUMPAD_PLUS", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.show_one_level",
                    {"type": "NUMPAD_MINUS", "value": "PRESS"},
                    {
                        "properties": [
                            ("open", False),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "outliner.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "outliner.expanded_toggle",
                    {"type": "A", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "outliner.keyingset_add_selected",
                    {"type": "K", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.keyingset_remove_selected",
                    {"type": "K", "value": "PRESS", "alt": True},
                    None,
                ),
                ("anim.keyframe_insert", {"type": "I", "value": "PRESS"}, None),
                (
                    "anim.keyframe_delete",
                    {"type": "I", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "outliner.drivers_add_selected",
                    {"type": "D", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "outliner.drivers_add_selected",
                    {"type": "D", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "outliner.drivers_delete_selected",
                    {"type": "D", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "outliner.drivers_delete_selected",
                    {"type": "D", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("outliner.collection_new", {"type": "C", "value": "PRESS"}, None),
                ("outliner.delete", {"type": "X", "value": "PRESS"}, None),
                ("outliner.delete", {"type": "DEL", "value": "PRESS"}, None),
                ("object.move_to_collection", {"type": "M", "value": "PRESS"}, None),
                (
                    "object.link_to_collection",
                    {"type": "M", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "outliner.collection_exclude_set",
                    {"type": "E", "value": "PRESS"},
                    None,
                ),
                (
                    "outliner.collection_exclude_clear",
                    {"type": "E", "value": "PRESS", "alt": True},
                    None,
                ),
                ("outliner.hide", {"type": "H", "value": "PRESS"}, None),
                (
                    "outliner.unhide_all",
                    {"type": "H", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "outliner.id_copy",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "outliner.id_copy",
                    {"type": "C", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "outliner.id_paste",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "outliner.id_paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
            ],
        },
    ),
    (
        "Property Editor",
        {"space_type": "PROPERTIES", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "buttons.context_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("direction", "PREV"),
                        ],
                    },
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "PREV"),
                        ],
                    },
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("direction", "NEXT"),
                        ],
                    },
                ),
                (
                    "screen.space_context_cycle",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("direction", "NEXT"),
                        ],
                    },
                ),
                (
                    "buttons.start_filter",
                    {"type": "F", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "buttons.start_filter",
                    {"type": "F", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "buttons.clear_filter",
                    {"type": "F", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "object.modifier_set_active",
                    {"type": "LEFTMOUSE", "value": "PRESS"},
                    None,
                ),
                (
                    "object.modifier_remove",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.modifier_remove",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.modifier_copy",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "object.modifier_apply",
                    {"type": "A", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.modifier_apply",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.gpencil_modifier_remove",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.gpencil_modifier_remove",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.gpencil_modifier_copy",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "object.gpencil_modifier_apply",
                    {"type": "A", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.gpencil_modifier_apply",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.shaderfx_remove",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.shaderfx_remove",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "object.shaderfx_copy",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "constraint.delete",
                    {"type": "X", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "constraint.delete",
                    {"type": "DEL", "value": "PRESS"},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "constraint.copy",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "constraint.apply",
                    {"type": "A", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
                (
                    "constraint.apply",
                    {"type": "A", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("report", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Sequencer",
        {"space_type": "SEQUENCE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.split",
                    {"type": "K", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "SOFT"),
                        ],
                    },
                ),
                (
                    "sequencer.split",
                    {"type": "K", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("type", "HARD"),
                        ],
                    },
                ),
                (
                    "sequencer.mute",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "sequencer.mute",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "sequencer.unmute",
                    {"type": "H", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "sequencer.unmute",
                    {"type": "H", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                ("sequencer.lock", {"type": "H", "value": "PRESS", "ctrl": True}, None),
                (
                    "sequencer.unlock",
                    {"type": "H", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "sequencer.unlock",
                    {"type": "H", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("sequencer.reassign_inputs", {"type": "R", "value": "PRESS"}, None),
                (
                    "sequencer.reload",
                    {"type": "R", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.reload",
                    {"type": "R", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("adjust_length", True),
                        ],
                    },
                ),
                (
                    "sequencer.offset_clear",
                    {"type": "O", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.duplicate_move",
                    {"type": "D", "value": "PRESS", "shift": True},
                    None,
                ),
                ("sequencer.delete", {"type": "X", "value": "PRESS"}, None),
                ("sequencer.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "sequencer.copy",
                    {"type": "C", "value": "PRESS", "oskey": True},
                    None,
                ),
                ("sequencer.copy", {"type": "C", "value": "PRESS", "ctrl": True}, None),
                (
                    "sequencer.paste",
                    {"type": "V", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "sequencer.paste",
                    {"type": "V", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("keep_offset", True),
                        ],
                    },
                ),
                (
                    "sequencer.paste",
                    {"type": "V", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("keep_offset", True),
                        ],
                    },
                ),
                ("sequencer.images_separate", {"type": "Y", "value": "PRESS"}, None),
                ("sequencer.meta_toggle", {"type": "TAB", "value": "PRESS"}, None),
                (
                    "sequencer.meta_make",
                    {"type": "G", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "sequencer.meta_make",
                    {"type": "G", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.meta_separate",
                    {"type": "G", "value": "PRESS", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "sequencer.meta_separate",
                    {"type": "G", "value": "PRESS", "ctrl": True, "alt": True},
                    None,
                ),
                ("sequencer.view_all", {"type": "HOME", "value": "PRESS"}, None),
                (
                    "sequencer.view_all",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                (
                    "sequencer.view_selected",
                    {"type": "NUMPAD_PERIOD", "value": "PRESS"},
                    None,
                ),
                ("sequencer.view_frame", {"type": "NUMPAD_0", "value": "PRESS"}, None),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_UP", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("next", True),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_DOWN", "value": "PRESS", "repeat": True},
                    {
                        "properties": [
                            ("next", False),
                            ("center", False),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {"type": "PAGE_UP", "value": "PRESS", "alt": True, "repeat": True},
                    {
                        "properties": [
                            ("next", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.strip_jump",
                    {
                        "type": "PAGE_DOWN",
                        "value": "PRESS",
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("next", False),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.swap",
                    {
                        "type": "LEFT_ARROW",
                        "value": "PRESS",
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("side", "LEFT"),
                        ],
                    },
                ),
                (
                    "sequencer.swap",
                    {
                        "type": "RIGHT_ARROW",
                        "value": "PRESS",
                        "alt": True,
                        "repeat": True,
                    },
                    {
                        "properties": [
                            ("side", "RIGHT"),
                        ],
                    },
                ),
                (
                    "sequencer.gap_remove",
                    {"type": "BACK_SPACE", "value": "PRESS"},
                    {
                        "properties": [
                            ("all", False),
                        ],
                    },
                ),
                (
                    "sequencer.gap_remove",
                    {"type": "BACK_SPACE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("all", True),
                        ],
                    },
                ),
                (
                    "sequencer.gap_insert",
                    {"type": "EQUAL", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sequencer.snap",
                    {"type": "S", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "sequencer.swap_inputs",
                    {"type": "S", "value": "PRESS", "alt": True},
                    None,
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 1),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 2),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 3),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 4),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "FIVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 5),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "SIX", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 6),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "SEVEN", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 7),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "EIGHT", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 8),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "NINE", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 9),
                        ],
                    },
                ),
                (
                    "sequencer.split_multicam",
                    {"type": "ZERO", "value": "PRESS"},
                    {
                        "properties": [
                            ("camera", 10),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    {
                        "properties": [
                            ("linked_handle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_handle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                            ("linked_time", True),
                            ("side_of_frame", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "sequencer.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "sequencer.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "sequencer.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                ("sequencer.select_linked_pick", {"type": "L", "value": "PRESS"}, None),
                (
                    "sequencer.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_linked",
                    {"type": "L", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "sequencer.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY"},
                    {
                        "properties": [
                            ("mode", "SET"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                            ("tweak", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "EVT_TWEAK_L", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "SUB"),
                            ("tweak", True),
                        ],
                    },
                ),
                ("sequencer.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "sequencer.select_box",
                    {"type": "B", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("include_handles", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_box",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("include_handles", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_grouped",
                    {"type": "G", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "A", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_add"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "C", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_change"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_view_pie"),
                        ],
                    },
                ),
                ("sequencer.slip", {"type": "S", "value": "PRESS"}, None),
                (
                    "wm.context_set_int",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "scene.sequence_editor.overlay_frame"),
                            ("value", 0),
                        ],
                    },
                ),
                ("transform.seq_slide", {"type": "G", "value": "PRESS"}, None),
                ("transform.seq_slide", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                (
                    "transform.transform",
                    {"type": "E", "value": "PRESS"},
                    {
                        "properties": [
                            ("mode", "TIME_EXTEND"),
                        ],
                    },
                ),
                ("marker.add", {"type": "M", "value": "PRESS"}, None),
                ("marker.rename", {"type": "M", "value": "PRESS", "ctrl": True}, None),
                (
                    "sequencer.select_side_of_frame",
                    {"type": "LEFT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("side", "LEFT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_side_of_frame",
                    {"type": "RIGHT_BRACKET", "value": "PRESS"},
                    {
                        "properties": [
                            ("side", "RIGHT"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap_sequencer"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_context_menu"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "SequencerPreview",
        {"space_type": "SEQUENCE_EDITOR", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("toggle", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.select",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("toggle", True),
                            ("center", True),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "sequencer.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("sequencer.select_box", {"type": "B", "value": "PRESS"}, None),
                (
                    "sequencer.view_all_preview",
                    {"type": "HOME", "value": "PRESS"},
                    None,
                ),
                (
                    "sequencer.view_all_preview",
                    {"type": "NDOF_BUTTON_FIT", "value": "PRESS"},
                    None,
                ),
                ("sequencer.view_ghost_border", {"type": "O", "value": "PRESS"}, None),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 8.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 4.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("ratio", 2.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_1", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 1.0),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_2", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.5),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_4", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.25),
                        ],
                    },
                ),
                (
                    "sequencer.view_zoom_ratio",
                    {"type": "NUMPAD_8", "value": "PRESS"},
                    {
                        "properties": [
                            ("ratio", 0.125),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "ACCENT_GRAVE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_preview_view_pie"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "sequencer.strip_transform_clear",
                    {"type": "G", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("property", "POSITION"),
                        ],
                    },
                ),
                (
                    "sequencer.strip_transform_clear",
                    {"type": "S", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("property", "SCALE"),
                        ],
                    },
                ),
                (
                    "sequencer.strip_transform_clear",
                    {"type": "R", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("property", "ROTATION"),
                        ],
                    },
                ),
                ("sequencer.delete", {"type": "X", "value": "PRESS"}, None),
                ("sequencer.delete", {"type": "DEL", "value": "PRESS"}, None),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_preview_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_preview_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "ACCENT_GRAVE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_gizmo"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "PERIOD", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "SEQUENCER_MT_pivot_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "Z", "value": "PRESS", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("data_path", "space_data.show_overlays"),
                        ],
                    },
                ),
                (
                    "sequencer.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "Spreadsheet Generic",
        {"space_type": "SPREADSHEET", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "wm.context_toggle",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_ui"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "Y", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "space_data.show_region_channels"),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "UV Editor",
        {"space_type": "EMPTY", "region_type": "WINDOW"},
        {
            "items": [
                (
                    "zenuv.call_popup",
                    {"type": "U", "value": "PRESS", "shift": True},
                    None,
                ),
                ("zenuv.call_pie", {"type": "U", "value": "PRESS", "alt": True}, None),
                (
                    "wm.call_menu_pie",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "MACHIN3_MT_uv_align_pie"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "ONE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "VERT"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "TWO", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "EDGE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                (
                    "mesh.select_mode",
                    {"type": "THREE", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("use_extend", True),
                            ("use_expand", True),
                            ("type", "FACE"),
                        ],
                    },
                ),
                ("mesh.select_mode", {"type": "FOUR", "value": "PRESS"}, None),
                (
                    "wm.context_set_enum",
                    {"type": "ONE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "VERTEX"),
                        ],
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "TWO", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "EDGE"),
                        ],
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "THREE", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "FACE"),
                        ],
                    },
                ),
                (
                    "wm.context_set_enum",
                    {"type": "FOUR", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.uv_select_mode"),
                            ("value", "ISLAND"),
                        ],
                    },
                ),
                (
                    "uv.select",
                    {"type": "LEFTMOUSE", "value": "CLICK"},
                    {
                        "properties": [
                            ("deselect_all", True),
                        ],
                    },
                ),
                (
                    "uv.select",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                ("uv.mark_seam", {"type": "E", "value": "PRESS", "oskey": True}, None),
                ("uv.mark_seam", {"type": "E", "value": "PRESS", "ctrl": True}, None),
                (
                    "uv.select_loop",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True},
                    None,
                ),
                (
                    "uv.select_loop",
                    {"type": "LEFTMOUSE", "value": "CLICK", "shift": True, "alt": True},
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "uv.select_edge_ring",
                    {"type": "LEFTMOUSE", "value": "CLICK", "alt": True, "oskey": True},
                    None,
                ),
                (
                    "uv.select_edge_ring",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True, "alt": True},
                    None,
                ),
                (
                    "uv.select_edge_ring",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "uv.select_edge_ring",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    {
                        "properties": [
                            ("extend", True),
                        ],
                    },
                ),
                (
                    "uv.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "oskey": True},
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    },
                ),
                (
                    "uv.shortest_path_pick",
                    {"type": "LEFTMOUSE", "value": "CLICK", "ctrl": True},
                    {
                        "properties": [
                            ("use_fill", False),
                        ],
                    },
                ),
                (
                    "uv.shortest_path_pick",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("use_fill", True),
                        ],
                    },
                ),
                (
                    "uv.shortest_path_pick",
                    {
                        "type": "LEFTMOUSE",
                        "value": "CLICK",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("use_fill", True),
                        ],
                    },
                ),
                ("uv.select_split", {"type": "Y", "value": "PRESS"}, None),
                (
                    "uv.select_box",
                    {"type": "B", "value": "PRESS"},
                    {
                        "properties": [
                            ("pinned", False),
                        ],
                    },
                ),
                (
                    "uv.select_box",
                    {"type": "B", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("pinned", True),
                        ],
                    },
                ),
                (
                    "uv.select_box",
                    {"type": "B", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("pinned", True),
                        ],
                    },
                ),
                ("uv.select_circle", {"type": "C", "value": "PRESS"}, None),
                (
                    "uv.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "oskey": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "uv.select_lasso",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "ctrl": True},
                    {
                        "properties": [
                            ("mode", "ADD"),
                        ],
                    },
                ),
                (
                    "uv.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "oskey": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "uv.select_lasso",
                    {
                        "type": "EVT_TWEAK_R",
                        "value": "ANY",
                        "shift": True,
                        "ctrl": True,
                    },
                    {
                        "properties": [
                            ("mode", "SUB"),
                        ],
                    },
                ),
                (
                    "uv.select_linked",
                    {"type": "L", "value": "PRESS", "oskey": True},
                    None,
                ),
                (
                    "uv.select_linked",
                    {"type": "L", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "uv.select_linked_pick",
                    {"type": "L", "value": "PRESS"},
                    {
                        "properties": [
                            ("extend", True),
                            ("deselect", False),
                        ],
                    },
                ),
                (
                    "uv.select_linked_pick",
                    {"type": "L", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("deselect", True),
                        ],
                    },
                ),
                (
                    "uv.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "uv.select_more",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "uv.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "oskey": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "uv.select_less",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "ctrl": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "PRESS"},
                    {
                        "properties": [
                            ("action", "SELECT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "I", "value": "PRESS", "oskey": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "I", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("action", "INVERT"),
                        ],
                    },
                ),
                (
                    "uv.select_all",
                    {"type": "A", "value": "DOUBLE_CLICK"},
                    {
                        "properties": [
                            ("action", "DESELECT"),
                        ],
                    },
                ),
                ("uv.reveal", {"type": "H", "value": "PRESS", "alt": True}, None),
                (
                    "uv.hide",
                    {"type": "H", "value": "PRESS"},
                    {
                        "properties": [
                            ("unselected", False),
                        ],
                    },
                ),
                (
                    "uv.hide",
                    {"type": "H", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("unselected", True),
                        ],
                    },
                ),
                (
                    "uv.select_pinned",
                    {"type": "P", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_merge"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "M", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_split"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "W", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_align"),
                        ],
                    },
                ),
                ("uv.stitch", {"type": "V", "value": "PRESS", "alt": True}, None),
                ("uv.rip_move", {"type": "V", "value": "PRESS"}, None),
                (
                    "uv.pin",
                    {"type": "P", "value": "PRESS"},
                    {
                        "properties": [
                            ("clear", False),
                        ],
                    },
                ),
                (
                    "uv.pin",
                    {"type": "P", "value": "PRESS", "alt": True},
                    {
                        "properties": [
                            ("clear", True),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "U", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_unwrap"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "S", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_snap_pie"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "TAB", "value": "PRESS", "ctrl": True},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_select_mode"),
                        ],
                    },
                ),
                (
                    "wm.call_menu_pie",
                    {"type": "O", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("name", "VIEW3D_MT_proportional_editing_falloff_pie"),
                        ],
                    },
                ),
                (
                    "wm.context_toggle",
                    {"type": "O", "value": "PRESS"},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_proportional_edit"),
                        ],
                    },
                ),
                ("transform.translate", {"type": "EVT_TWEAK_L", "value": "ANY"}, None),
                ("transform.translate", {"type": "G", "value": "PRESS"}, None),
                ("transform.rotate", {"type": "R", "value": "PRESS"}, None),
                ("transform.resize", {"type": "S", "value": "PRESS"}, None),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "alt": True,
                        "oskey": True,
                    },
                    None,
                ),
                (
                    "transform.shear",
                    {
                        "type": "S",
                        "value": "PRESS",
                        "shift": True,
                        "ctrl": True,
                        "alt": True,
                    },
                    None,
                ),
                (
                    "transform.mirror",
                    {"type": "M", "value": "PRESS", "ctrl": True},
                    None,
                ),
                (
                    "wm.context_toggle",
                    {"type": "TAB", "value": "PRESS", "shift": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.use_snap"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "TAB", "value": "PRESS", "shift": True, "oskey": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.snap_uv_element"),
                        ],
                    },
                ),
                (
                    "wm.context_menu_enum",
                    {"type": "TAB", "value": "PRESS", "shift": True, "ctrl": True},
                    {
                        "properties": [
                            ("data_path", "tool_settings.snap_uv_element"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "RIGHTMOUSE", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_context_menu"),
                        ],
                    },
                ),
                (
                    "wm.call_menu",
                    {"type": "APP", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "IMAGE_MT_uvs_context_menu"),
                        ],
                    },
                ),
                (
                    "uv.cursor_set",
                    {"type": "RIGHTMOUSE", "value": "PRESS", "shift": True},
                    None,
                ),
                (
                    "transform.translate",
                    {"type": "EVT_TWEAK_R", "value": "ANY", "shift": True},
                    {
                        "properties": [
                            ("cursor_transform", True),
                            ("release_confirm", True),
                        ],
                    },
                ),
                (
                    "wm.tool_set_by_id",
                    {"type": "W", "value": "PRESS"},
                    {
                        "properties": [
                            ("name", "builtin.select_box"),
                            ("cycle", True),
                        ],
                    },
                ),
            ],
        },
    ),
    (
        "View3D Walk Modal",
        {"space_type": "EMPTY", "region_type": "WINDOW", "modal": True},
        {
            "items": [
                ("CANCEL", {"type": "RIGHTMOUSE", "value": "ANY", "any": True}, None),
                (
                    "CANCEL",
                    {"type": "ESC", "value": "PRESS", "any": True, "repeat": True},
                    None,
                ),
                ("CONFIRM", {"type": "LEFTMOUSE", "value": "ANY", "any": True}, None),
                (
                    "CONFIRM",
                    {"type": "RET", "value": "PRESS", "any": True, "repeat": True},
                    None,
                ),
                (
                    "CONFIRM",
                    {
                        "type": "NUMPAD_ENTER",
                        "value": "PRESS",
                        "any": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "FAST_ENABLE",
                    {
                        "type": "LEFT_SHIFT",
                        "value": "PRESS",
                        "any": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "FAST_DISABLE",
                    {"type": "LEFT_SHIFT", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "SLOW_ENABLE",
                    {"type": "LEFT_ALT", "value": "PRESS", "any": True, "repeat": True},
                    None,
                ),
                (
                    "SLOW_DISABLE",
                    {"type": "LEFT_ALT", "value": "RELEASE", "any": True},
                    None,
                ),
                ("FORWARD", {"type": "COMMA", "value": "PRESS", "repeat": True}, None),
                ("BACKWARD", {"type": "O", "value": "PRESS", "repeat": True}, None),
                ("LEFT", {"type": "A", "value": "PRESS", "repeat": True}, None),
                ("RIGHT", {"type": "E", "value": "PRESS", "repeat": True}, None),
                ("UP", {"type": "PERIOD", "value": "PRESS", "repeat": True}, None),
                ("DOWN", {"type": "QUOTE", "value": "PRESS", "repeat": True}, None),
                ("FORWARD_STOP", {"type": "COMMA", "value": "RELEASE"}, None),
                ("BACKWARD_STOP", {"type": "O", "value": "RELEASE"}, None),
                ("LEFT_STOP", {"type": "A", "value": "RELEASE"}, None),
                ("RIGHT_STOP", {"type": "E", "value": "RELEASE"}, None),
                ("UP_STOP", {"type": "PERIOD", "value": "RELEASE"}, None),
                ("DOWN_STOP", {"type": "QUOTE", "value": "RELEASE"}, None),
                (
                    "FORWARD",
                    {"type": "UP_ARROW", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "BACKWARD",
                    {"type": "DOWN_ARROW", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "LEFT",
                    {"type": "LEFT_ARROW", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "RIGHT",
                    {"type": "RIGHT_ARROW", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "FORWARD_STOP",
                    {"type": "UP_ARROW", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "BACKWARD_STOP",
                    {"type": "DOWN_ARROW", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "LEFT_STOP",
                    {"type": "LEFT_ARROW", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "RIGHT_STOP",
                    {"type": "RIGHT_ARROW", "value": "RELEASE", "any": True},
                    None,
                ),
                (
                    "GRAVITY_TOGGLE",
                    {"type": "TAB", "value": "PRESS", "repeat": True},
                    None,
                ),
                (
                    "GRAVITY_TOGGLE",
                    {"type": "G", "value": "PRESS", "repeat": True},
                    None,
                ),
                ("JUMP", {"type": "SPACE", "value": "PRESS", "repeat": True}, None),
                ("JUMP_STOP", {"type": "SPACE", "value": "RELEASE"}, None),
                ("TELEPORT", {"type": "J", "value": "PRESS", "repeat": True}, None),
                (
                    "TELEPORT",
                    {"type": "MIDDLEMOUSE", "value": "ANY", "any": True},
                    None,
                ),
                (
                    "ACCELERATE",
                    {
                        "type": "NUMPAD_PLUS",
                        "value": "PRESS",
                        "any": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "DECELERATE",
                    {
                        "type": "NUMPAD_MINUS",
                        "value": "PRESS",
                        "any": True,
                        "repeat": True,
                    },
                    None,
                ),
                (
                    "ACCELERATE",
                    {"type": "WHEELUPMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
                (
                    "DECELERATE",
                    {"type": "WHEELDOWNMOUSE", "value": "PRESS", "any": True},
                    None,
                ),
            ],
        },
    ),
]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version

    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data

    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
