if (True) exitWith {hint "True!"};

if (False) then {
    hint "True!";
} else {
    hint "False"
};

private _strEqual = if (False) then {"Yes"} else {"No"};
hint _strEqual;