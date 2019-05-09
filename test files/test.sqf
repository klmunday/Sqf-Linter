private ["_trees","_tree","_treeType","_cutSpeed","_woodAmount","_itemName","_diff","_ui","_progress","_pgText","_cP"];
if (life_action_inUse) exitWith {};
if ((vehicle player) != player) exitWith {};
if (player distance2D cursorObject > 3) exitWith {};
if (player getVariable "restrained") exitWith {hint localize "STR_NOTF_isrestrained";};
if (player getVariable "playerSurrender") exitWith {hint localize "STR_NOTF_surrender";};
life_action_inUse = true;

_tree = cursorObject;
_treeType = [_tree] call life_fnc_getModelName;

if (True) then {
    switch (_treeType) do {
        case "t_ficus_small_f": {_cutSpeed = 0.10; _woodAmount = 1;};
        case "t_ficus_medium_f": {_cutSpeed = 0.20; _woodAmount = 3;};
        case "t_cyathea_f": {_cutSpeed = 0.15; _woodAmount = 2;};
        case "t_leucaena_f": {_cutSpeed = 0.10; _woodAmount = 1;};
        case "t_palaquium_f": {_cutSpeed = 0.25; _woodAmount = 4;};
        case "t_cocosnucifera2s_small_f": {_cutSpeed = 0.20; _woodAmount = 3;};
        case "t_cocosnucifera3s_tall_f": {_cutSpeed = 0.25; _woodAmount = 4;};
        case "t_agathis_wide_f": {_cutSpeed = 0.15; _woodAmount = 2;};
        case "t_agathis_tall_f": {_cutSpeed = 0.20; _woodAmount = 3;};
        case "t_albizia_f": {_cutSpeed = 0.15; _woodAmount = 2;};
        default {_cutSpeed = 0.15; _woodAmount = 2;};
    };

    _diff = ["wood_log",_woodAmount,life_carryWeight,life_maxWeight] call life_fnc_calWeightDiff;
    if (_diff isEqualTo 0) exitWith {
        hint localize "STR_NOTF_InvFull";
        life_action_inUse = false;
    };

    //Setup our progress bar.
    disableSerialization;
    5 cutRsc ["life_progress","PLAIN"];
    _ui = uiNamespace getVariable "life_progress";
    _progress = _ui displayCtrl 38201;
    _pgText = _ui displayCtrl 38202;
    _pgText ctrlSetText format["%2 (1%1)...","%", localize "STR_GatherAction_Tree"];
    _progress progressSetPosition 0.01;
    _cP = 0.01;

    for "_i" from 0 to 1 step 0 do {
        if (animationState player != "AinvPknlMstpSnonWnonDnon_medic_1") then { // find better animation?
            [player,"AinvPknlMstpSnonWnonDnon_medic_1",true] remoteExecCall ["life_fnc_animSync",2];
            player switchMove "AinvPknlMstpSnonWnonDnon_medic_1";
            player playMoveNow "AinvPknlMstpSnonWnonDnon_medic_1";
            [player,"woodCut",50] remoteExecCall ["life_fnc_say3D",-2,false];
        };

        sleep  _cutSpeed;
        _cP = _cP + 0.01;
        _progress progressSetPosition _cP;
        _pgText ctrlSetText format["%3 (%1%2)...",round(_cP * 100),"%", localize "STR_GatherAction_Tree"];
        if (_cP >= 1) exitWith {};
        if (!alive player) exitWith {};
        if (player != vehicle player) exitWith {};
        if (life_interrupted) exitWith {};
    };

    life_action_inUse = false;
    5 cutText ["","PLAIN"];
    player playActionNow "stop";
    if (life_interrupted) exitWith {life_interrupted = false; titleText[localize "STR_NOTF_ActionCancel","PLAIN"];};
    if (player distance2D _tree > 3) exitWith {hint localize "STR_NOTF_TREE_ToFar";};

    [true,"wood_Log",_diff] call life_fnc_handleInv;
    titleText[format[localize "STR_NOTF_Harvest_Success",(localize "STR_Item_WoodLog"),_diff],"PLAIN"];

    [_tree] remoteExec ["TON_fnc_hideTree"];

} else {
    hint localize "STR_NOTF_Woodaxe";
};

life_action_inUse = false;