private _test = 5;
if (True) then {
    systemChat str _test;
};
globalVar = "hello " + "world";

uiNamespace setVariable ["namespaceVar", "test"];
parsingNamespace setVariable ["publicVar", "hello", True];

private _localVersion = parsingNamespace getVariable ["publicVar", "default"];

with uiNamespace do {
    hint namespaceVar;
};

hint globalVar;
