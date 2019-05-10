if (True) then {hint "True!"};

if (False) then {
    "test" systemChat;
} else {
    [] call {hint "test"};
};

private _strEqual = if (False) else {"test"}
hint _strEqual;