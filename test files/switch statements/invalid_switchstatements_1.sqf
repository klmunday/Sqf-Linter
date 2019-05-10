private _value = 2;
switch (_value) do {
    case 1: { hint "value is 1" };
    case 2: { hint "value is 2" };
    case 3: { hint "value is 3" };
    default hint "value is 0";
};

private _test = switch (_value) {
    case "test": {1};
    case 2: {2};
    default {"no value"};
};