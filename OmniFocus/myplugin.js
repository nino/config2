/*{
    "author": "Author Name",
    "targets": ["omnifocus"],
    "type": "action",
    "identifier": "com.mycompany.Come on this should work please",
    "version": "0.1",
    "description": "A plug-in that...",
    "label": "Come on this should work please",
    "mediumLabel": "Come on this should work please",
    "paletteLabel": "Come on this should work please",
}*/
import { Lib } from './lib.js'

const TO_BE_EXPORTED = new PlugIn.Action(function(selection) {
    // Add code to run when the action is invoked
    console.log("Invoked with selection", selection);
    new Alert("Message", Lib.msg).show();
});

