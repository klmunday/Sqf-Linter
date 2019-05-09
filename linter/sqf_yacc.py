import ply.yacc as pyacc
from classes.namespace import Namespace
import sys
from linter.sqf_lex import tokens
from linter.sqf_linter import global_var_handler
from classes.var_handler import VarHandler

var_handler = VarHandler()

terminators = {
    ';': 0,
    ',': 0,
}
is_interpreting = True  # This indicates whether the parser should pass the code as if it was being executed

literals = []

engine_functions = {'#', 'abs', 'acos', 'actionids', 'actionkeys', 'actionkeysimages', 'actionkeysnames', 'actionkeysnamesarray', 'actionname', 'activateaddons', 'activatekey', 'add3denconnection', 'add3deneventhandler', 'addcamshake', 'addforcegeneratorrtd', 'additempool', 'addmagazinepool', 'addmissioneventhandler', 'addmusiceventhandler', 'addswitchableunit', 'addtoremainscollector', 'addweaponpool', 'admin', 'agent', 'agltoasl', 'aimpos', 'airdensityrtd', 'airplanethrottle', 'airportside', 'aisfinishheal', 'alive', 'allcontrols', 'allmissionobjects', 'allsimpleobjects', 'allturrets', 'allturrets', 'allvariables', 'allvariables', 'allvariables', 'allvariables', 'allvariables', 'allvariables', 'allvariables', 'animationnames', 'animationstate', 'asin', 'asltoagl', 'asltoatl', 'assert', 'assignedcargo', 'assignedcommander', 'assigneddriver', 'assignedgunner', 'assigneditems', 'assignedtarget', 'assignedteam', 'assignedvehicle', 'assignedvehiclerole', 'atan', 'atg', 'atltoasl', 'attachedobject', 'attachedobjects', 'attachedto', 'attackenabled', 'backpack', 'backpackcargo', 'backpackcontainer', 'backpackitems', 'backpackmagazines', 'behaviour', 'binocular', 'boundingcenter', 'breakto', 'buldozer_enableroaddiag', 'buldozer_loadnewroads', 'buttonaction', 'buttonaction', 'calculateplayervisibilitybyfriendly', 'camcommitted', 'camdestroy', 'cameraeffectenablehud', 'camerainterest', 'campreloaded', 'camtarget', 'camusenvg', 'cancelsimpletaskdestination', 'canfire', 'canmove', 'canstand', 'cantriggerdynamicsimulation', 'canunloadincombat', 'captive', 'captivenum', 'case', 'cbchecked', 'ceil', 'channelenabled', 'checkaifeature', 'classname', 'clear3deninventory', 'clearallitemsfrombackpack', 'clearbackpackcargo', 'clearbackpackcargoglobal', 'cleargroupicons', 'clearitemcargo', 'clearitemcargoglobal', 'clearmagazinecargo', 'clearmagazinecargoglobal', 'clearoverlay', 'clearweaponcargo', 'clearweaponcargoglobal', 'closedialog', 'closeoverlay', 'collapseobjecttree', 'collect3denhistory', 'collectivertd', 'combatmode', 'commander', 'commandgetout', 'commandstop', 'comment', 'commitoverlay', 'compile', 'compilefinal', 'completedfsm', 'composetext', 'confighierarchy', 'configname', 'configproperties', 'configsourceaddonlist', 'configsourcemod', 'configsourcemodlist', 'copytoclipboard', 'cos', 'create3dencomposition', 'createagent', 'createcenter', 'createdialog', 'creatediarylink', 'creategeardialog', 'creategroup', 'createguardedpoint', 'createlocation', 'createmarker', 'createmarkerlocal', 'createmine', 'createsimpleobject', 'createsoundsource', 'createteam', 'createtrigger', 'createvehiclecrew', 'crew', 'ctaddheader', 'ctaddrow', 'ctclear', 'ctcursel', 'ctheadercount', 'ctrlactivate', 'ctrlangle', 'ctrlautoscrolldelay', 'ctrlautoscrollrewind', 'ctrlautoscrollspeed', 'ctrlclassname', 'ctrlcommitted', 'ctrldelete', 'ctrlenabled', 'ctrlenabled', 'ctrlfade', 'ctrlhtmlloaded', 'ctrlidc', 'ctrlidd', 'ctrlmapanimclear', 'ctrlmapanimcommit', 'ctrlmapanimdone', 'ctrlmapmouseover', 'ctrlmapscale', 'ctrlmodel', 'ctrlmodeldirandup', 'ctrlmodelscale', 'ctrlparent', 'ctrlparentcontrolsgroup', 'ctrlposition', 'ctrlscale', 'ctrlsetfocus', 'ctrlshown', 'ctrltext', 'ctrltext', 'ctrltextheight', 'ctrltextsecondary', 'ctrltextwidth', 'ctrltype', 'ctrlvisible', 'ctrowcount', 'curatoraddons', 'curatorcameraarea', 'curatorcameraareaceiling', 'curatoreditableobjects', 'curatoreditingarea', 'curatoreditingareatype', 'curatorpoints', 'curatorregisteredobjects', 'curatorwaypointcost', 'currentcommand', 'currentmagazine', 'currentmagazinedetail', 'currentmuzzle', 'currenttask', 'currenttasks', 'currentthrowable', 'currentvisionmode', 'currentwaypoint', 'currentweapon', 'currentweaponmode', 'currentzeroing', 'damage', 'datetonumber', 'deactivatekey', 'debriefingtext', 'debuglog', 'decaygraphvalues', 'default', 'deg', 'delete3denentities', 'deletecenter', 'deletecollection', 'deletegroup', 'deleteidentity', 'deletelocation', 'deletemarker', 'deletemarkerlocal', 'deletesite', 'deletestatus', 'deleteteam', 'deletevehicle', 'deletewaypoint', 'detach', 'detectedmines', 'diag_captureframe', 'diag_captureframetofile', 'diag_captureslowframe', 'diag_codeperformance', 'diag_dynamicsimulationend', 'diag_lightnewload', 'diag_log', 'diag_logslowframe', 'diag_setlightnew', 'didjipowner', 'difficultyenabled', 'difficultyoption', 'direction', 'direction', 'disablemapindicators', 'disableremotesensors', 'disableuserinput', 'displayparent', 'dissolveteam', 'do3denaction', 'dogetout', 'dostop', 'drawicon3d', 'drawline3d', 'driver', 'drop', 'dynamicsimulationdistance', 'dynamicsimulationdistancecoef', 'dynamicsimulationenabled', 'dynamicsimulationenabled', 'echo', 'edit3denmissionattributes', 'effectivecommander', 'enableaudiofeature', 'enablecamshake', 'enablecaustics', 'enabledebriefingstats', 'enablediaglegend', 'enabledynamicsimulationsystem', 'enableengineartillery', 'enableenvironment', 'enableradio', 'enablesatnormalondetail', 'enablesaving', 'enablesentences', 'enablestressdamage', 'enableteamswitch', 'enabletraffic', 'endmission', 'enginesisonrtd', 'enginespowerrtd', 'enginesrpmrtd', 'enginestorquertd', 'entities', 'entities', 'estimatedtimeleft', 'everybackpack', 'everycontainer', 'exp', 'expecteddestination', 'exportjipmessages', 'eyedirection', 'eyepos', 'face', 'faction', 'failmission', 'fillweaponsfrompool', 'finddisplay', 'finite', 'firstbackpack', 'flag', 'flaganimationphase', 'flagowner', 'flagside', 'flagtexture', 'fleeing', 'floor', 'forceatpositionrtd', 'forcegeneratorrtd', 'forcemap', 'forcerespawn', 'format', 'formation', 'formation', 'formationdirection', 'formationleader', 'formationmembers', 'formationposition', 'formationtask', 'formattext', 'formleader', 'fromeditor', 'fuel', 'fullcrew', 'fullcrew', 'gearidcammocount', 'gearslotammocount', 'gearslotdata', 'get3denactionstate', 'get3denconnections', 'get3denentity', 'get3denentityid', 'get3dengrid', 'get3denlayerentities', 'get3denselected', 'getaimingcoef', 'getallenvsoundcontrollers', 'getallhitpointsdamage', 'getallownedmines', 'getallsoundcontrollers', 'getammocargo', 'getanimaimprecision', 'getanimspeedcoef', 'getarray', 'getartilleryammo', 'getassignedcuratorlogic', 'getassignedcuratorunit', 'getbackpackcargo', 'getbleedingremaining', 'getburningvalue', 'getcameraviewdirection', 'getcenterofmass', 'getconnecteduav', 'getcontainermaxload', 'getcustomaimcoef', 'getcustomsoundcontroller', 'getcustomsoundcontrollercount', 'getdammage', 'getdescription', 'getdirvisual', 'getdlcassetsusagebyname', 'getdlcs', 'getdlcusagetime', 'geteditorcamera', 'geteditormode', 'getenginetargetrpmrtd', 'getfatigue', 'getfieldmanualstartpage', 'getforcedflagtexture', 'getfuelcargo', 'getgraphvalues', 'getgroupiconparams', 'getgroupicons', 'getitemcargo', 'getmagazinecargo', 'getmarkercolor', 'getmarkerpos', 'getmarkerpos', 'getmarkersize', 'getmarkertype', 'getmass', 'getmissionconfig', 'getmissionconfigvalue', 'getmissionlayerentities', 'getmodelinfo', 'getnumber', 'getobjectdlc', 'getobjectmaterials', 'getobjecttextures', 'getobjecttype', 'getoxygenremaining', 'getpersonuseddlcs', 'getpilotcameradirection', 'getpilotcameraposition', 'getpilotcamerarotation', 'getpilotcameratarget', 'getplatenumber', 'getplayerchannel', 'getplayerscores', 'getplayeruid', 'getpos', 'getposasl', 'getposaslvisual', 'getposaslw', 'getposatl', 'getposatlvisual', 'getposvisual', 'getposworld', 'getpylonmagazines', 'getrepaircargo', 'getrotorbrakertd', 'getshotparents', 'getslingload', 'getstamina', 'getstatvalue', 'getsuppression', 'getterrainheightasl', 'gettext', 'gettrimoffsetrtd', 'getunitloadout', 'getunitloadout', 'getunitloadout', 'getusermfdtext', 'getusermfdvalue', 'getvehiclecargo', 'getweaponcargo', 'getweaponsway', 'getwingsorientationrtd', 'getwingspositionrtd', 'getwppos', 'goggles', 'goto', 'group', 'groupfromnetid', 'groupid', 'groupowner', 'groupselectedunits', 'gunner', 'handgunitems', 'handgunmagazine', 'handgunweapon', 'handshit', 'haspilotcamera', 'hcallgroups', 'hcleader', 'hcremoveallgroups', 'hcselected', 'hcshowbar', 'headgear', 'hidebody', 'hideobjectglobal', 'hint', 'hintcadet', 'hintsilent', 'hmd', 'hostmission', 'image', 'importallgroups', 'importance', 'incapacitatedstate', 'inflamed', 'infopanel', 'infopanels', 'ingameuiseteventhandler', 'inheritsfrom', 'inputaction', 'isabletobreathe', 'isagent', 'isaimprecisionenabled', 'isarray', 'isautohoveron', 'isautonomous', 'isautostartupenabledrtd', 'isautotrimonrtd', 'isbleeding', 'isburning', 'isclass', 'iscollisionlighton', 'iscopilotenabled', 'isdamageallowed', 'isdlcavailable', 'isengineon', 'isforcedwalk', 'isformationleader', 'isgroupdeletedwhenempty', 'ishidden', 'isinremainscollector', 'iskeyactive', 'islaseron', 'islighton', 'islocalized', 'ismanualfire', 'ismarkedforcollection', 'isnil', 'isnull', 'isnull', 'isnull', 'isnull', 'isnull', 'isnull', 'isnull', 'isnull', 'isnull', 'isnumber', 'isobjecthidden', 'isobjectrtd', 'isonroad', 'isplayer', 'isrealtime', 'isshowing3dicons', 'issimpleobject', 'issprintallowed', 'isstaminaenabled', 'istext', 'istouchingground', 'isturnedout', 'isuavconnected', 'isvehiclecargo', 'isvehicleradaron', 'iswalking', 'isweapondeployed', 'isweaponrested', 'itemcargo', 'items', 'itemswithmagazines', 'keyimage', 'keyname', 'landresult', 'lasertarget', 'lbclear', 'lbclear', 'lbcolorright', 'lbcursel', 'lbcursel', 'lbdelete', 'lbpictureright', 'lbselection', 'lbsetcolorright', 'lbsetdata', 'lbsetpicturecolor', 'lbsetpicturecolorselected', 'lbsetselectcolor', 'lbsettext', 'lbsetvalue', 'lbsize', 'lbsize', 'lbsort', 'lbsort', 'lbsort', 'lbsortbyvalue', 'lbsortbyvalue', 'lbtextright', 'leader', 'leader', 'leader', 'leaderboarddeinit', 'leaderboardgetrows', 'leaderboardinit', 'leaderboardrequestrowsfriends', 'leaderboardrequestrowsglobal', 'leaderboardrequestrowsglobalarounduser', 'leaderboardsrequestuploadscore', 'leaderboardsrequestuploadscorekeepbest', 'leaderboardstate', 'lifestate', 'lightdetachobject', 'lightison', 'linearconversion', 'lineintersects', 'lineintersectsobjs', 'lineintersectssurfaces', 'lineintersectswith', 'list', 'listremotetargets', 'listvehiclesensors', 'ln', 'lnbaddarray', 'lnbaddrow', 'lnbclear', 'lnbclear', 'lnbcolorright', 'lnbcurselrow', 'lnbcurselrow', 'lnbdeletecolumn', 'lnbgetcolumnsposition', 'lnbgetcolumnsposition', 'lnbpictureright', 'lnbsetcolorright', 'lnbsetcurselrow', 'lnbsetpicture', 'lnbsetpicturecolorright', 'lnbsetpicturecolorselectedright', 'lnbsettext', 'lnbsettooltip', 'lnbsize', 'lnbsize', 'lnbsortbyvalue', 'lnbtextright', 'load', 'loadabs', 'loadbackpack', 'loadfile', 'loaduniform', 'loadvest', 'local', 'local', 'localize', 'locationposition', 'locked', 'lockeddriver', 'lockidentity', 'log', 'lognetwork', 'lognetworkterminate', 'magazinecargo', 'magazines', 'magazinesallturrets', 'magazinesammo', 'magazinesammocargo', 'magazinesammofull', 'magazinesdetail', 'magazinesdetailbackpack', 'magazinesdetailuniform', 'magazinesdetailvest', 'mapanimadd', 'mapgridposition', 'markeralpha', 'markerbrush', 'markercolor', 'markerdir', 'markerpos', 'markerpos', 'markershape', 'markersize', 'markertext', 'markertype', 'matrixtranspose', 'members', 'menuadd', 'menuclear', 'menuclear', 'menudata', 'menuenable', 'menuexpand', 'menuhover', 'menuhover', 'menusetaction', 'menusetdata', 'menusetvalue', 'menushortcuttext', 'menusort', 'menuurl', 'mineactive', 'missiletarget', 'missiletargetpos', 'modparams', 'moonphase', 'morale', 'move3dencamera', 'moveout', 'movetime', 'movetocompleted', 'movetofailed', 'name', 'name', 'namesound', 'nearestbuilding', 'nearestbuilding', 'nearestlocation', 'nearestlocations', 'nearestlocationwithdubbing', 'nearestobjects', 'nearestterrainobjects', 'needreload', 'netid', 'netid', 'nextmenuitemindex', 'not', 'numberofenginesrtd', 'numbertodate', 'objectcurators', 'objectfromnetid', 'objectparent', 'onbriefinggroup', 'onbriefingnotes', 'onbriefingplan', 'onbriefingteamswitch', 'oncommandmodechanged', 'oneachframe', 'ongroupiconclick', 'ongroupiconoverenter', 'ongroupiconoverleave', 'onhcgroupselectionchanged', 'onplayerconnected', 'onplayerdisconnected', 'onpreloadfinished', 'onpreloadstarted', 'onteamswitch', 'opendlcpage', 'openmap', 'openmap', 'opensteamapp', 'openyoutubevideo', 'owner', 'params', 'parsenumber', 'parsenumber', 'parsesimplearray', 'parsetext', 'pickweaponpool', 'pitch', 'playableslotsnumber', 'playersnumber', 'playmission', 'playmusic', 'playmusic', 'playscriptedmission', 'playsound', 'playsound', 'playsound3d', 'position', 'position', 'positioncameratoworld', 'ppeffectcommitted', 'ppeffectcommitted', 'ppeffectcreate', 'ppeffectdestroy', 'ppeffectdestroy', 'ppeffectenabled', 'precision', 'preloadcamera', 'preloadsound', 'preloadtitleobj', 'preloadtitlersc', 'preprocessfile', 'preprocessfilelinenumbers', 'primaryweapon', 'primaryweaponitems', 'primaryweaponmagazine', 'priority', 'processdiarylink', 'progressloadingscreen', 'progressposition', 'publicvariable', 'publicvariableserver', 'putweaponpool', 'queryitemspool', 'querymagazinepool', 'queryweaponpool', 'rad', 'radiochannelcreate', 'random', 'rank', 'rankid', 'rating', 'rectangular', 'registeredtasks', 'reload', 'reloadenabled', 'remoteexeccall', 'remove3denconnection', 'remove3deneventhandler', 'remove3denlayer', 'removeall3deneventhandlers', 'removeallactions', 'removeallassigneditems', 'removeallcontainers', 'removeallcuratoraddons', 'removeallcuratorcameraareas', 'removeallcuratoreditingareas', 'removeallhandgunitems', 'removeallitems', 'removeallitemswithmagazines', 'removeallmissioneventhandlers', 'removeallmusiceventhandlers', 'removeallownedmines', 'removeallprimaryweaponitems', 'removeallweapons', 'removebackpack', 'removebackpackglobal', 'removefromremainscollector', 'removegoggles', 'removeheadgear', 'removemissioneventhandler', 'removemusiceventhandler', 'removeswitchableunit', 'removeuniform', 'removevest', 'requiredversion', 'resetsubgroupdirection', 'resources', 'restarteditorcamera', 'reverse', 'roadat', 'roadsconnectedto', 'roledescription', 'ropeattachedobjects', 'ropeattachedto', 'ropeattachenabled', 'ropecreate', 'ropecut', 'ropedestroy', 'ropeendposition', 'ropelength', 'ropes', 'ropeunwind', 'ropeunwound', 'rotorsforcesrtd', 'rotorsrpmrtd', 'round', 'save3deninventory', 'saveoverlay', 'savevar', 'scopename', 'score', 'scoreside', 'screenshot', 'screentoworld', 'scriptdone', 'scriptname', 'scudstate', 'secondaryweapon', 'secondaryweaponitems', 'secondaryweaponmagazine', 'selectbestplaces', 'selectededitorobjects', 'selectionnames', 'selectmax', 'selectmin', 'selectplayer', 'selectrandom', 'sendaumessage', 'sendudpmessage', 'servercommandavailable', 'servercommandexecutable', 'set3denattributes', 'set3dengrid', 'set3deniconsvisible', 'set3denlinesvisible', 'set3denmissionattributes', 'set3denmodelsvisible', 'set3denselected', 'setacctime', 'setaperture', 'setaperturenew', 'setarmorypoints', 'setcamshakedefparams', 'setcamshakeparams', 'setcompassoscillation', 'setcurrentchannel', 'setcustommissiondata', 'setcustomsoundcontroller', 'setdate', 'setdefaultcamera', 'setdetailmapblendpars', 'setgroupiconsselectable', 'setgroupiconsvisible', 'sethorizonparallaxcoef', 'sethudmovementlevels', 'setinfopanel', 'setlocalwindparams', 'setmouseposition', 'setmusiceventhandler', 'setobjectviewdistance', 'setobjectviewdistance', 'setplayable', 'setplayerrespawntime', 'setshadowdistance', 'setsimulweatherlayers', 'setstaminascheme', 'setstatvalue', 'setsystemofunits', 'setterraingrid', 'settimemultiplier', 'settrafficdensity', 'settrafficdistance', 'settrafficgap', 'settrafficspeed', 'setviewdistance', 'setwind', 'showchat', 'showcinemaborder', 'showcommandingmenu', 'showcompass', 'showcuratorcompass', 'showgps', 'showhud', 'showhud', 'showmap', 'showpad', 'showradio', 'showscoretable', 'showsubtitles', 'showuavfeed', 'showwarrant', 'showwatch', 'showwaypoints', 'side', 'side', 'side', 'simpletasks', 'simulationenabled', 'simulclouddensity', 'simulcloudocclusion', 'simulinclouds', 'sin', 'size', 'sizeof', 'skiptime', 'sleep', 'sliderposition', 'sliderposition', 'sliderrange', 'sliderrange', 'slidersetrange', 'sliderspeed', 'sliderspeed', 'soldiermagazines', 'someammo', 'speaker', 'speed', 'speedmode', 'sqrt', 'squadparams', 'stance', 'startloadingscreen', 'stopenginertd', 'stopped', 'str', 'supportinfo', 'surfaceiswater', 'surfacenormal', 'surfacetype', 'synchronizedobjects', 'synchronizedtriggers', 'synchronizedwaypoints', 'synchronizedwaypoints', 'systemchat', 'tan', 'taskalwaysvisible', 'taskchildren', 'taskcompleted', 'taskcustomdata', 'taskdescription', 'taskdestination', 'taskhint', 'taskmarkeroffset', 'taskparent', 'taskresult', 'taskstate', 'tasktype', 'teammember', 'teamname', 'teamtype', 'terminate', 'terrainintersect', 'terrainintersectasl', 'terrainintersectatasl', 'text', 'text', 'textlog', 'textlogformat', 'tg', 'titlecut', 'titlefadeout', 'titleobj', 'titlersc', 'titletext', 'toarray', 'tolower', 'tostring', 'toupper', 'triggeractivated', 'triggeractivation', 'triggerammo', 'triggerarea', 'triggerattachedvehicle', 'triggerstatements', 'triggertext', 'triggertimeout', 'triggertimeoutcurrent', 'triggertype', 'tvadd', 'tvclear', 'tvclear', 'tvcollapseall', 'tvcollapseall', 'tvcursel', 'tvcursel', 'tvdelete', 'tvexpandall', 'tvexpandall', 'tvpictureright', 'tvsetdata', 'tvsetpicturecolor', 'tvsetpicturerightcolor', 'tvsettooltip', 'tvsort', 'tvtext', 'tvvalue', 'type', 'type', 'typename', 'typeof', 'uavcontrol', 'uisleep', 'unassigncurator', 'unassignteam', 'unassignvehicle', 'underwater', 'uniform', 'uniformcontainer', 'uniformitems', 'uniformmagazines', 'unitaddons', 'unitaimposition', 'unitaimpositionvisual', 'unitbackpack', 'unitisuav', 'unitpos', 'unitready', 'unitrecoilcoefficient', 'units', 'units', 'unlockachievement', 'updateobjecttree', 'useaiopermapobstructiontest', 'useaisteeringcomponent', 'vectordir', 'vectordirvisual', 'vectorlinearconversion', 'vectormagnitude', 'vectormagnitudesqr', 'vectornormalized', 'vectorup', 'vectorupvisual', 'vehicle', 'vehiclecargoenabled', 'vehiclereceiveremotetargets', 'vehiclereportownposition', 'vehiclereportremotetargets', 'vehiclevarname', 'velocity', 'velocitymodelspace', 'verifysignature', 'vest', 'vestcontainer', 'vestitems', 'vestmagazines', 'visibleposition', 'visiblepositionasl', 'waituntil', 'waypointattachedobject', 'waypointattachedvehicle', 'waypointbehaviour', 'waypointcombatmode', 'waypointcompletionradius', 'waypointdescription', 'waypointforcebehaviour', 'waypointformation', 'waypointhouseposition', 'waypointloiterradius', 'waypointloitertype', 'waypointname', 'waypointposition', 'waypoints', 'waypointscript', 'waypointsenableduav', 'waypointshow', 'waypointspeed', 'waypointstatements', 'waypointtimeout', 'waypointtimeoutcurrent', 'waypointtype', 'waypointvisible', 'weaponcargo', 'weaponinertia', 'weaponlowered', 'weapons', 'weaponsitems', 'weaponsitemscargo', 'weaponstate', 'weaponstate', 'weightrtd', 'wfsidetext', 'wfsidetext', 'wfsidetext', 'wingsforcesrtd', 'worldtoscreen', 'action', 'actionparams', 'add3denlayer', 'addaction', 'addbackpack', 'addbackpackcargo', 'addbackpackcargoglobal', 'addbackpackglobal', 'addcuratoraddons', 'addcuratorcameraarea', 'addcuratoreditableobjects', 'addcuratoreditingarea', 'addcuratorpoints', 'addeditorobject', 'addeventhandler', 'addforce', 'addgoggles', 'addgroupicon', 'addhandgunitem', 'addheadgear', 'additem', 'additemcargo', 'additemcargoglobal', 'additemtobackpack', 'additemtouniform', 'additemtovest', 'addlivestats', 'addmagazine', 'addmagazine', 'addmagazineammocargo', 'addmagazinecargo', 'addmagazinecargoglobal', 'addmagazineglobal', 'addmagazines', 'addmagazineturret', 'addmenu', 'addmenuitem', 'addmpeventhandler', 'addownedmine', 'addplayerscores', 'addprimaryweaponitem', 'addpublicvariableeventhandler', 'addpublicvariableeventhandler', 'addrating', 'addresources', 'addscore', 'addscoreside', 'addsecondaryweaponitem', 'addteammember', 'addtorque', 'adduniform', 'addvehicle', 'addvest', 'addwaypoint', 'addweapon', 'addweaponcargo', 'addweaponcargoglobal', 'addweaponglobal', 'addweaponitem', 'addweaponturret', 'aimedattarget', 'allow3dmode', 'allowcrewinimmobile', 'allowcuratorlogicignoreareas', 'allowdamage', 'allowdammage', 'allowfileoperations', 'allowfleeing', 'allowgetin', 'allowsprint', 'ammo', 'ammoonpylon', 'and', 'and', 'animate', 'animatebay', 'animatedoor', 'animatepylon', 'animatesource', 'animationphase', 'animationsourcephase', 'append', 'apply', 'arrayintersect', 'assignascargo', 'assignascargoindex', 'assignascommander', 'assignasdriver', 'assignasgunner', 'assignasturret', 'assigncurator', 'assignitem', 'assignteam', 'assigntoairport', 'atan2', 'attachobject', 'attachto', 'backpackspacefor', 'bezierinterpolation', 'boundingbox', 'boundingboxreal', 'breakout', 'buildingexit', 'buildingpos', 'buttonsetaction', 'call', 'callextension', 'callextension', 'camcommand', 'camcommit', 'camcommitprepared', 'camconstuctionsetparams', 'camcreate', 'cameraeffect', 'campreload', 'campreparebank', 'campreparedir', 'campreparedive', 'campreparefocus', 'campreparefov', 'campreparefovrange', 'campreparepos', 'campreparerelpos', 'campreparetarget', 'campreparetarget', 'camsetbank', 'camsetdir', 'camsetdive', 'camsetfocus', 'camsetfov', 'camsetfovrange', 'camsetpos', 'camsetrelpos', 'camsettarget', 'camsettarget', 'canadd', 'canadditemtobackpack', 'canadditemtouniform', 'canadditemtovest', 'canslingload', 'canvehiclecargo', 'catch', 'cbsetchecked', 'checkvisibility', 'clear3denattribute', 'closedisplay', 'commandartilleryfire', 'commandchat', 'commandfire', 'commandfollow', 'commandfsm', 'commandmove', 'commandradio', 'commandsuppressivefire', 'commandtarget', 'commandwatch', 'commandwatch', 'configclasses', 'confirmsensortarget', 'connectterminaltouav', 'controlsgroupctrl', 'copywaypoints', 'count', 'countenemy', 'countfriendly', 'countside', 'counttype', 'countunknown', 'create3denentity', 'creatediaryrecord', 'creatediarysubject', 'createdisplay', 'createmenu', 'createmissiondisplay', 'createmissiondisplay', 'creatempcampaigndisplay', 'createsimpletask', 'createsite', 'createtask', 'createunit', 'createunit', 'createvehicle', 'createvehiclelocal', 'ctdata', 'ctfindheaderrows', 'ctfindrowheader', 'ctheadercontrols', 'ctremoveheaders', 'ctremoverows', 'ctrladdeventhandler', 'ctrlanimatemodel', 'ctrlanimationphasemodel', 'ctrlchecked', 'ctrlcommit', 'ctrlcreate', 'ctrlenable', 'ctrlmapanimadd', 'ctrlmapcursor', 'ctrlmapscreentoworld', 'ctrlmapworldtoscreen', 'ctrlremovealleventhandlers', 'ctrlremoveeventhandler', 'ctrlsetactivecolor', 'ctrlsetangle', 'ctrlsetautoscrolldelay', 'ctrlsetautoscrollrewind', 'ctrlsetautoscrollspeed', 'ctrlsetbackgroundcolor', 'ctrlsetchecked', 'ctrlsetchecked', 'ctrlsetdisabledcolor', 'ctrlseteventhandler', 'ctrlsetfade', 'ctrlsetfont', 'ctrlsetfonth1', 'ctrlsetfonth1b', 'ctrlsetfonth2', 'ctrlsetfonth2b', 'ctrlsetfonth3', 'ctrlsetfonth3b', 'ctrlsetfonth4', 'ctrlsetfonth4b', 'ctrlsetfonth5', 'ctrlsetfonth5b', 'ctrlsetfonth6', 'ctrlsetfonth6b', 'ctrlsetfontheight', 'ctrlsetfontheighth1', 'ctrlsetfontheighth2', 'ctrlsetfontheighth3', 'ctrlsetfontheighth4', 'ctrlsetfontheighth5', 'ctrlsetfontheighth6', 'ctrlsetfontheightsecondary', 'ctrlsetfontp', 'ctrlsetfontp', 'ctrlsetfontpb', 'ctrlsetfontsecondary', 'ctrlsetforegroundcolor', 'ctrlsetmodel', 'ctrlsetmodeldirandup', 'ctrlsetmodelscale', 'ctrlsetpixelprecision', 'ctrlsetpixelprecision', 'ctrlsetposition', 'ctrlsetpositionh', 'ctrlsetpositionw', 'ctrlsetpositionx', 'ctrlsetpositiony', 'ctrlsetscale', 'ctrlsetstructuredtext', 'ctrlsettext', 'ctrlsettextcolor', 'ctrlsettextcolorsecondary', 'ctrlsettextsecondary', 'ctrlsettooltip', 'ctrlsettooltipcolorbox', 'ctrlsettooltipcolorshade', 'ctrlsettooltipcolortext', 'ctrlshow', 'ctrowcontrols', 'ctsetcursel', 'ctsetdata', 'ctsetheadertemplate', 'ctsetrowtemplate', 'ctsetvalue', 'ctvalue', 'curatorcoef', 'currentmagazinedetailturret', 'currentmagazineturret', 'currentweaponturret', 'customchat', 'customradio', 'cutfadeout', 'cutfadeout', 'cutobj', 'cutobj', 'cutrsc', 'cutrsc', 'cuttext', 'cuttext', 'debugfsm', 'deleteat', 'deleteeditorobject', 'deletegroupwhenempty', 'deleterange', 'deleteresources', 'deletevehiclecrew', 'diarysubjectexists', 'directsay', 'disableai', 'disablecollisionwith', 'disableconversation', 'disablenvgequipment', 'disabletiequipment', 'disableuavconnectability', 'displayaddeventhandler', 'displayctrl', 'displayremovealleventhandlers', 'displayremoveeventhandler', 'displayseteventhandler', 'distance', 'distance', 'distance', 'distance', 'distance2d', 'distancesqr', 'distancesqr', 'distancesqr', 'distancesqr', 'doartilleryfire', 'dofire', 'dofollow', 'dofsm', 'domove', 'doorphase', 'dosuppressivefire', 'dotarget', 'dowatch', 'dowatch', 'drawarrow', 'drawellipse', 'drawicon', 'drawline', 'drawlink', 'drawlocation', 'drawpolygon', 'drawrectangle', 'drawtriangle', 'editobject', 'editorseteventhandler', 'emptypositions', 'enableai', 'enableaifeature', 'enableaimprecision', 'enableattack', 'enableautostartuprtd', 'enableautotrimrtd', 'enablechannel', 'enablechannel', 'enablecollisionwith', 'enablecopilot', 'enabledynamicsimulation', 'enabledynamicsimulation', 'enablefatigue', 'enablegunlights', 'enableinfopanelcomponent', 'enableirlasers', 'enablemimics', 'enablepersonturret', 'enablereload', 'enableropeattach', 'enablesimulation', 'enablesimulationglobal', 'enablestamina', 'enableuavconnectability', 'enableuavwaypoints', 'enablevehiclecargo', 'enablevehiclesensor', 'enableweapondisassembly', 'engineon', 'evalobjectargument', 'exec', 'execeditorscript', 'execfsm', 'execvm', 'fademusic', 'faderadio', 'fadesound', 'fadespeech', 'find', 'find', 'findcover', 'findeditorobject', 'findeditorobject', 'findemptyposition', 'findemptypositionready', 'findif', 'findnearestenemy', 'fire', 'fire', 'fireattarget', 'flyinheight', 'flyinheightasl', 'forceadduniform', 'forceflagtexture', 'forcefollowroad', 'forcespeed', 'forcewalk', 'forceweaponfire', 'foreachmember', 'foreachmemberagent', 'foreachmemberteam', 'forgettarget', 'get3denattribute', 'get3denattribute', 'get3denattribute', 'get3denattribute', 'get3denattribute', 'get3denmissionattribute', 'getartilleryeta', 'getcargoindex', 'getcompatiblepylonmagazines', 'getcompatiblepylonmagazines', 'getdir', 'geteditorobjectscope', 'getenvsoundcontroller', 'getfriend', 'getfsmvariable', 'getgroupicon', 'gethidefrom', 'gethit', 'gethitindex', 'gethitpointdamage', 'getobjectargument', 'getobjectchildren', 'getobjectproxy', 'getpos', 'getreldir', 'getrelpos', 'getsoundcontroller', 'getsoundcontrollerresult', 'getspeed', 'getunittrait', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'getvariable', 'glanceat', 'globalchat', 'globalradio', 'groupchat', 'groupradio', 'groupselectunit', 'hasweapon', 'hcgroupparams', 'hcremovegroup', 'hcselectgroup', 'hcsetgroup', 'hideobject', 'hideobjectglobal', 'hideselection', 'hintc', 'hintc', 'hintc', 'htmlload', 'in', 'in', 'in', 'inarea', 'inarea', 'inarea', 'inarea', 'inarea', 'inareaarray', 'inareaarray', 'inareaarray', 'inareaarray', 'inflame', 'infopanelcomponentenabled', 'infopanelcomponents', 'inpolygon', 'inrangeofartillery', 'inserteditorobject', 'intersect', 'isequalto', 'isequaltype', 'isequaltypeall', 'isequaltypeany', 'isequaltypearray', 'isequaltypeparams', 'isflashlighton', 'isflatempty', 'isirlaseron', 'iskindof', 'iskindof', 'iskindof', 'issensortargetconfirmed', 'isuavconnectable', 'isuniformallowed', 'isvehiclesensorenabled', 'join', 'joinas', 'joinassilent', 'joinsilent', 'joinstring', 'kbadddatabase', 'kbadddatabasetargets', 'kbaddtopic', 'kbhastopic', 'kbreact', 'kbremovetopic', 'kbtell', 'kbwassaid', 'knowsabout', 'knowsabout', 'land', 'landat', 'lbadd', 'lbcolor', 'lbcolorright', 'lbdata', 'lbdelete', 'lbisselected', 'lbpicture', 'lbpictureright', 'lbsetcolor', 'lbsetcolorright', 'lbsetcursel', 'lbsetdata', 'lbsetpicture', 'lbsetpicturecolor', 'lbsetpicturecolordisabled', 'lbsetpicturecolorselected', 'lbsetpictureright', 'lbsetpicturerightcolor', 'lbsetpicturerightcolordisabled', 'lbsetpicturerightcolorselected', 'lbsetselectcolor', 'lbsetselectcolorright', 'lbsetselected', 'lbsettext', 'lbsettextright', 'lbsettooltip', 'lbsetvalue', 'lbtext', 'lbtextright', 'lbvalue', 'leavevehicle', 'leavevehicle', 'lightattachobject', 'limitspeed', 'linkitem', 'listobjects', 'lnbaddcolumn', 'lnbaddrow', 'lnbcolor', 'lnbcolorright', 'lnbdata', 'lnbdeletecolumn', 'lnbdeleterow', 'lnbpicture', 'lnbpictureright', 'lnbsetcolor', 'lnbsetcolorright', 'lnbsetcolumnspos', 'lnbsetcurselrow', 'lnbsetdata', 'lnbsetpicture', 'lnbsetpicturecolor', 'lnbsetpicturecolorright', 'lnbsetpicturecolorselected', 'lnbsetpicturecolorselectedright', 'lnbsetpictureright', 'lnbsettext', 'lnbsettextright', 'lnbsettooltip', 'lnbsetvalue', 'lnbsort', 'lnbsortbyvalue', 'lnbtext', 'lnbtextright', 'lnbvalue', 'loadidentity', 'loadmagazine', 'loadoverlay', 'loadstatus', 'lock', 'lock', 'lockcamerato', 'lockcargo', 'lockcargo', 'lockdriver', 'lockedcargo', 'lockedturret', 'lockturret', 'lockwp', 'lookat', 'lookatpos', 'magazinesturret', 'magazineturretammo', 'mapcenteroncamera', 'matrixmultiply', 'max', 'menuaction', 'menuadd', 'menuchecked', 'menucollapse', 'menudata', 'menudelete', 'menuenable', 'menuenabled', 'menuexpand', 'menupicture', 'menusetaction', 'menusetcheck', 'menusetdata', 'menusetpicture', 'menusetvalue', 'menushortcut', 'menushortcuttext', 'menusize', 'menusort', 'menutext', 'menuurl', 'menuvalue', 'min', 'minedetectedby', 'mod', 'modeltoworld', 'modeltoworldvisual', 'modeltoworldvisualworld', 'modeltoworldworld', 'move', 'moveinany', 'moveincargo', 'moveincargo', 'moveincommander', 'moveindriver', 'moveingunner', 'moveinturret', 'moveobjecttoend', 'moveto', 'nearentities', 'nearestobject', 'nearestobject', 'nearobjects', 'nearobjectsready', 'nearroads', 'nearsupplies', 'neartargets', 'newoverlay', 'nmenuitems', 'objstatus', 'ondoubleclick', 'onmapsingleclick', 'onshownewobject', 'or', 'or', 'ordergetin', 'param', 'params', 'playaction', 'playactionnow', 'playgesture', 'playmove', 'playmovenow', 'posscreentoworld', 'posworldtoscreen', 'ppeffectadjust', 'ppeffectadjust', 'ppeffectcommit', 'ppeffectcommit', 'ppeffectcommit', 'ppeffectenable', 'ppeffectenable', 'ppeffectenable', 'ppeffectforceinnvg', 'preloadobject', 'progresssetposition', 'publicvariableclient', 'pushback', 'pushbackunique', 'radiochanneladd', 'radiochannelremove', 'radiochannelsetcallsign', 'radiochannelsetlabel', 'random', 'registertask', 'remotecontrol', 'remoteexec', 'remoteexeccall', 'removeaction', 'removealleventhandlers', 'removeallmpeventhandlers', 'removecuratoraddons', 'removecuratorcameraarea', 'removecuratoreditableobjects', 'removecuratoreditingarea', 'removedrawicon', 'removedrawlinks', 'removeeventhandler', 'removegroupicon', 'removehandgunitem', 'removeitem', 'removeitemfrombackpack', 'removeitemfromuniform', 'removeitemfromvest', 'removeitems', 'removemagazine', 'removemagazineglobal', 'removemagazines', 'removemagazinesturret', 'removemagazineturret', 'removemenuitem', 'removemenuitem', 'removempeventhandler', 'removeownedmine', 'removeprimaryweaponitem', 'removesecondaryweaponitem', 'removesimpletask', 'removeteammember', 'removeweapon', 'removeweaponattachmentcargo', 'removeweaponcargo', 'removeweaponglobal', 'removeweaponturret', 'reportremotetarget', 'resize', 'respawnvehicle', 'reveal', 'reveal', 'revealmine', 'ropeattachto', 'ropedetach', 'saveidentity', 'savestatus', 'say', 'say', 'say2d', 'say2d', 'say3d', 'say3d', 'select', 'select', 'select', 'select', 'select', 'select', 'selectdiarysubject', 'selecteditorobject', 'selectionposition', 'selectleader', 'selectrandomweighted', 'selectweapon', 'selectweaponturret', 'sendsimplecommand', 'sendtask', 'sendtaskresult', 'servercommand', 'set', 'set3denattribute', 'set3denlayer', 'set3denlogictype', 'set3denmissionattribute', 'set3denobjecttype', 'setactualcollectivertd', 'setairplanethrottle', 'setairportside', 'setammo', 'setammocargo', 'setammoonpylon', 'setanimspeedcoef', 'setattributes', 'setautonomous', 'setbehaviour', 'setbehaviourstrong', 'setbleedingremaining', 'setbrakesrtd', 'setcamerainterest', 'setcamuseti', 'setcaptive', 'setcenterofmass', 'setcollisionlight', 'setcombatmode', 'setcombatmode', 'setconvoyseparation', 'setcuratorcameraareaceiling', 'setcuratorcoef', 'setcuratoreditingareatype', 'setcuratorwaypointcost', 'setcurrenttask', 'setcurrentwaypoint', 'setcustomaimcoef', 'setcustomweightrtd', 'setdamage', 'setdammage', 'setdebriefingtext', 'setdestination', 'setdir', 'setdirection', 'setdrawicon', 'setdriveonpath', 'setdropinterval', 'setdynamicsimulationdistance', 'setdynamicsimulationdistancecoef', 'seteditormode', 'seteditorobjectscope', 'seteffectcondition', 'setenginerpmrtd', 'setface', 'setfaceanimation', 'setfatigue', 'setfeaturetype', 'setflaganimationphase', 'setflagowner', 'setflagside', 'setflagtexture', 'setfog', 'setforcegeneratorrtd', 'setformation', 'setformation', 'setformationtask', 'setformdir', 'setfriend', 'setfromeditor', 'setfsmvariable', 'setfuel', 'setfuelcargo', 'setgroupicon', 'setgroupiconparams', 'setgroupid', 'setgroupidglobal', 'setgroupowner', 'setgusts', 'sethidebehind', 'sethit', 'sethitindex', 'sethitpointdamage', 'setidentity', 'setimportance', 'setleader', 'setlightambient', 'setlightattenuation', 'setlightbrightness', 'setlightcolor', 'setlightdaylight', 'setlightflaremaxdistance', 'setlightflaresize', 'setlightintensity', 'setlightnings', 'setlightuseflare', 'setmagazineturretammo', 'setmarkeralpha', 'setmarkeralphalocal', 'setmarkerbrush', 'setmarkerbrushlocal', 'setmarkercolor', 'setmarkercolorlocal', 'setmarkerdir', 'setmarkerdirlocal', 'setmarkerpos', 'setmarkerposlocal', 'setmarkershape', 'setmarkershapelocal', 'setmarkersize', 'setmarkersizelocal', 'setmarkertext', 'setmarkertextlocal', 'setmarkertype', 'setmarkertypelocal', 'setmass', 'setmimic', 'setmissiletarget', 'setmissiletargetpos', 'setmusiceffect', 'setname', 'setname', 'setname', 'setnamesound', 'setobjectarguments', 'setobjectmaterial', 'setobjectmaterialglobal', 'setobjectproxy', 'setobjecttexture', 'setobjecttextureglobal', 'setovercast', 'setowner', 'setoxygenremaining', 'setparticlecircle', 'setparticleclass', 'setparticlefire', 'setparticleparams', 'setparticlerandom', 'setpilotcameradirection', 'setpilotcamerarotation', 'setpilotcameratarget', 'setpilotlight', 'setpipeffect', 'setpitch', 'setplatenumber', 'setpos', 'setposasl', 'setposasl2', 'setposaslw', 'setposatl', 'setposition', 'setposworld', 'setpylonloadout', 'setpylonspriority', 'setradiomsg', 'setrain', 'setrainbow', 'setrandomlip', 'setrank', 'setrectangular', 'setrepaircargo', 'setrotorbrakertd', 'setshotparents', 'setside', 'setsimpletaskalwaysvisible', 'setsimpletaskcustomdata', 'setsimpletaskdescription', 'setsimpletaskdestination', 'setsimpletasktarget', 'setsimpletasktype', 'setsize', 'setskill', 'setskill', 'setslingload', 'setsoundeffect', 'setspeaker', 'setspeech', 'setspeedmode', 'setstamina', 'setsuppression', 'settargetage', 'settaskmarkeroffset', 'settaskresult', 'settaskstate', 'settext', 'settitleeffect', 'settriggeractivation', 'settriggerarea', 'settriggerstatements', 'settriggertext', 'settriggertimeout', 'settriggertype', 'settype', 'setunconscious', 'setunitability', 'setunitloadout', 'setunitloadout', 'setunitloadout', 'setunitpos', 'setunitposweak', 'setunitrank', 'setunitrecoilcoefficient', 'setunittrait', 'setunloadincombat', 'setuseractiontext', 'setusermfdtext', 'setusermfdvalue', 'setvariable', 'setvariable', 'setvariable', 'setvariable', 'setvariable', 'setvariable', 'setvariable', 'setvariable', 'setvectordir', 'setvectordirandup', 'setvectorup', 'setvehicleammo', 'setvehicleammodef', 'setvehiclearmor', 'setvehiclecargo', 'setvehicleid', 'setvehiclelock', 'setvehicleposition', 'setvehicleradar', 'setvehiclereceiveremotetargets', 'setvehiclereportownposition', 'setvehiclereportremotetargets', 'setvehicletipars', 'setvehiclevarname', 'setvelocity', 'setvelocitymodelspace', 'setvelocitytransformation', 'setvisibleiftreecollapsed', 'setwantedrpmrtd', 'setwaves', 'setwaypointbehaviour', 'setwaypointcombatmode', 'setwaypointcompletionradius', 'setwaypointdescription', 'setwaypointforcebehaviour', 'setwaypointformation', 'setwaypointhouseposition', 'setwaypointloiterradius', 'setwaypointloitertype', 'setwaypointname', 'setwaypointposition', 'setwaypointscript', 'setwaypointspeed', 'setwaypointstatements', 'setwaypointtimeout', 'setwaypointtype', 'setwaypointvisible', 'setweaponreloadingtime', 'setwinddir', 'setwindforce', 'setwindstr', 'setwingforcescalertd', 'setwppos', 'show3dicons', 'showlegend', 'showneweditorobject', 'showwaypoint', 'sidechat', 'sideradio', 'skill', 'skillfinal', 'slidersetposition', 'slidersetrange', 'slidersetspeed', 'sort', 'spawn', 'splitstring', 'stop', 'suppressfor', 'swimindepth', 'switchaction', 'switchcamera', 'switchgesture', 'switchlight', 'switchmove', 'synchronizeobjectsadd', 'synchronizeobjectsremove', 'synchronizetrigger', 'synchronizewaypoint', 'synchronizewaypoint', 'targetknowledge', 'targets', 'targetsaggregate', 'targetsquery', 'then', 'throw', 'tofixed', 'triggerattachobject', 'triggerattachvehicle', 'triggerdynamicsimulation', 'try', 'turretlocal', 'turretowner', 'turretunit', 'tvadd', 'tvcollapse', 'tvcount', 'tvdata', 'tvdelete', 'tvexpand', 'tvpicture', 'tvpictureright', 'tvsetcolor', 'tvsetcursel', 'tvsetdata', 'tvsetpicture', 'tvsetpicturecolor', 'tvsetpicturecolordisabled', 'tvsetpicturecolorselected', 'tvsetpictureright', 'tvsetpicturerightcolor', 'tvsetpicturerightcolordisabled', 'tvsetpicturerightcolorselected', 'tvsetselectcolor', 'tvsettext', 'tvsettooltip', 'tvsetvalue', 'tvsort', 'tvsortbyvalue', 'tvtext', 'tvtooltip', 'tvvalue', 'unassignitem', 'unitsbelowheight', 'unitsbelowheight', 'unlinkitem', 'unregistertask', 'updatedrawicon', 'updatemenuitem', 'useaudiotimeformoves', 'vectoradd', 'vectorcos', 'vectorcrossproduct', 'vectordiff', 'vectordistance', 'vectordistancesqr', 'vectordotproduct', 'vectorfromto', 'vectormodeltoworld', 'vectormodeltoworldvisual', 'vectormultiply', 'vectorworldtomodel', 'vectorworldtomodelvisual', 'vehiclechat', 'vehicleradio', 'waypointattachobject', 'waypointattachvehicle', 'weaponaccessories', 'weaponaccessoriescargo', 'weapondirection', 'weaponsturret', 'worldtomodel', 'worldtomodelvisual', 'acctime', 'activatedaddons', 'agents', 'airdensitycurvertd', 'all3denentities', 'allairports', 'allcurators', 'allcutlayers', 'alldead', 'alldeadmen', 'alldisplays', 'allgroups', 'allmapmarkers', 'allmines', 'allplayers', 'allsites', 'allunits', 'allunitsuav', 'armorypoints', 'benchmark', 'blufor', 'briefingname', 'buldozer_isenabledroaddiag', 'buldozer_reloadopermap', 'cadetmode', 'cameraon', 'cameraview', 'campaignconfigfile', 'cansuspend', 'cheatsenabled', 'civilian', 'clearforcesrtd', 'clearitempool', 'clearmagazinepool', 'clearradio', 'clearweaponpool', 'clientowner', 'commandingmenu', 'configfile', 'confignull', 'controlnull', 'copyfromclipboard', 'curatorcamera', 'curatormouseover', 'curatorselected', 'current3denoperation', 'currentchannel', 'currentnamespace', 'cursorobject', 'cursortarget', 'customwaypointposition', 'date', 'daytime', 'diag_activemissionfsms', 'diag_activescripts', 'diag_activesqfscripts', 'diag_activesqsscripts', 'diag_fps', 'diag_fpsmin', 'diag_frameno', 'diag_ticktime', 'dialog', 'didjip', 'difficulty', 'difficultyenabledrtd', 'disabledebriefingstats', 'disableserialization', 'displaynull', 'distributionregion', 'dynamicsimulationsystemenabled', 'east', 'enableenddialog', 'endl', 'endloadingscreen', 'environmentenabled', 'estimatedendservertime', 'exit', 'false', 'finishmissioninit', 'fog', 'fogforecast', 'fogparams', 'forcedmap', 'forceend', 'forceweatherchange', 'freelook', 'get3dencamera', 'get3deniconsvisible', 'get3denlinesvisible', 'get3denmouseover', 'getartillerycomputersettings', 'getcalculateplayervisibilitybyfriendly', 'getclientstate', 'getclientstatenumber', 'getcursorobjectparams', 'getdlcassetsusage', 'getelevationoffset', 'getmissiondlcs', 'getmissionlayers', 'getmouseposition', 'getmusicplayedtime', 'getobjectviewdistance', 'getremotesensorsdisabled', 'getresolution', 'getshadowdistance', 'getterraingrid', 'gettotaldlcusagetime', 'groupiconselectable', 'groupiconsvisible', 'grpnull', 'gusts', 'halt', 'hasinterface', 'hcshownbar', 'hudmovementlevels', 'humidity', 'independent', 'initambientlife', 'is3den', 'is3denmultiplayer', 'isautotest', 'isdedicated', 'isfilepatchingenabled', 'isinstructorfigureenabled', 'ismultiplayer', 'ismultiplayersolo', 'ispipenabled', 'isremoteexecuted', 'isremoteexecutedjip', 'isserver', 'issteammission', 'isstreamfriendlyuienabled', 'isstressdamageenabled', 'istuthintsenabled', 'isuicontext', 'language', 'librarycredits', 'librarydisclaimers', 'lightnings', 'linebreak', 'loadgame', 'locationnull', 'logentities', 'mapanimclear', 'mapanimcommit', 'mapanimdone', 'markasfinishedonsteam', 'missionconfigfile', 'missiondifficulty', 'missionname', 'missionstart', 'missionversion', 'moonintensity', 'musicvolume', 'netobjnull', 'nextweatherchange', 'nil', 'objnull', 'opencuratorinterface', 'opfor', 'overcast', 'overcastforecast', 'particlesquality', 'pi', 'pixelgrid', 'pixelgridbase', 'pixelgridnouiscale', 'pixelh', 'pixelw', 'playableunits', 'player', 'playerrespawntime', 'playerside', 'productversion', 'profilename', 'profilenamesteam', 'radiovolume', 'rain', 'rainbow', 'remoteexecutedowner', 'resetcamshake', 'resistance', 'reversedmousey', 'runinitscript', 'safezoneh', 'safezonew', 'safezonewabs', 'safezonex', 'safezonexabs', 'safezoney', 'savegame', 'savejoysticks', 'saveprofilenamespace', 'savingenabled', 'scriptnull', 'selectnoplayer', 'servername', 'servertime', 'shownartillerycomputer', 'shownchat', 'showncompass', 'showncuratorcompass', 'showngps', 'shownhud', 'shownmap', 'shownpad', 'shownradio', 'shownscoretable', 'shownuavfeed', 'shownwarrant', 'shownwatch', 'sideambientlife', 'sideempty', 'sideenemy', 'sidefriendly', 'sidelogic', 'sideunknown', 'simulweathersync', 'slingloadassistantshown', 'soundvolume', 'sunormoon', 'switchableunits', 'systemofunits', 'tasknull', 'teammembernull', 'teams', 'teamswitch', 'teamswitchenabled', 'time', 'timemultiplier', 'true', 'userinputdisabled', 'vehicles', 'viewdistance', 'visiblecompass', 'visiblegps', 'visiblemap', 'visiblescoretable', 'visiblewatch', 'waves', 'west', 'wind', 'winddir', 'windrtd', 'windstr', 'worldname', 'worldsize'}

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'COMPARISON_OP', 'CONFIG_ACCESSOR_GTGT'),
    ('left', 'BINARY_OP', 'COLON'),
    ('left', 'ELSE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD', 'CONFIG_ACCESSOR_SLASH'),
    ('left', 'POW'),
    ('left', 'UNARY_OP'),
    ('left', 'NULAR_OP', 'VARIABLE', 'VALUE', 'BRACED_EXP'),
)


def p_code(p):
    """
    code    : empty
            | statement
            | statement terminator code
    """
    p[0] = p[len(p) - 1]


def p_statement(p):
    """
    statement   : controlstructure
                | assignment
                | binaryexp
                | nularexp
                | unaryexp
    """
    p[0] = p[1]


def p_terminator(p):
    """
    terminator  : SEMI_COLON
                | COMMA
    """
    terminators[p[1]] += 1
    if all(terminators.values()):
        semi_count = terminators.get(';')
        comma_count = terminators.get(',')
        if p[1] is not ';':
            print(f'WARNING: File contains mixed line terminators. "{p[1]}" seen on line: {p.lineno(1)}. '
                  f'Current count: (; {semi_count}), (, {comma_count}). '
                  f'Recommended to use ; as it is standard.', file=sys.stderr)


def p_controlstructure(p):
    """
    controlstructure    : ifstatement
                        | whileloop
                        | forloop
                        | withstatement
    """
    p[0] = p[1]


def p_helpertype(p):
    """
    helpertype  : iftype
                | whiletype
                | fortype
                | withtype
    """
    p[0] = p[1]


def p_iftype(p):
    """
    iftype : IF forloop_condition
    """
    p[0] = p[1]


def p_ifstatement(p):
    """
    ifstatement : iftype THEN bracedexp
                | iftype EXITWITH bracedexp
                | iftype THEN bracedexp ELSE bracedexp
    """
    p[0] = p[1]
    

def p_withtype(p):
    """
    withtype : WITH NAMESPACE
    """
    p[0] = Namespace(p[2])


def p_withstatementinit(p):
    """
    withstatementinit : withtype DO
    """
    if isinstance(p[1], Namespace):
        var_handler.change_namespace(p[1].value)
    else:
        print(f'WARNING: Possible error with WithType used on line: {p.lineno(1)}.')


def p_withstatement(p):
    """
    withstatement : withstatementinit bracedexp
    """
    p[0] = p[2]


def p_whiletype(p):
    """
    whiletype   : WHILE forloop_condition
    """


def p_whileloop(p):
    """
    whileloop : whiletype DO bracedexp
    """
    p[0] = p[3]


def p_fortype(p):
    """
    fortype : FOR new_scope string FROM primaryexp TO primaryexp
            | FOR new_scope string FROM primaryexp TO primaryexp STEP primaryexp
            | FOR new_scope LSPAREN bracedexp_noscope COMMA forloop_condition COMMA bracedexp_noscope RSPAREN
    """
    if p[3] != '[':
        if p[3][0] is '_':
            if var_handler.has_local_var(p[3]):
                if get_interpretation_state:
                    print(f'ERROR: Local variable {p[3]} already defined. Occurs on line: {p.lineno(3)}.', file=sys.stderr)
                p[0] = p[3]
            else:
                if not p[3][1].islower():
                    print(f'WARNING: Local variable {p[3]} defined with unconventional casing. on line: {p.lineno(3)}. '
                          f'Use lower case for the first character of local variables.', file=sys.stderr)
                var_handler.add_local_var(p[2], p.lineno(3))
        else:
            var_handler.add_global_var(p[1], p.lineno(1))


def p_forloop(p):
    """
    forloop : fortype DO bracedexp_noscope
    """
    pop_vars_and_warning_unused()
    p[0] = p[3]
    

def p_bracedexp_condition(p):
    """
    forloop_condition   : LBRACE booleanexp RBRACE
                        | identifier
    """
    if len(p) is 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_bracedexp_noscope(p):
    """
     bracedexp_noscope : LBRACE code RBRACE
    """
    p[0] = p[2]


def p_vardefinition(p):
    """
    vardefinition   : definition
                    | arraydefinition
    """


def p_assignment(p):
    """
    assignment  : assignment_code code RBRACE
                | definition EQUAL primaryexp
                | variable EQUAL primaryexp
    """
    if not var_handler.has_local_var(p[1]):
        var_handler.add_local_var(p[1], p.lineno(2))
    elif p[1] in engine_functions:
        print(f'ERROR: Engine function assignment attempted on line: {p.lineno(1)}. '
              f'Engine functions cannot be assigned to.', file=sys.stderr)
    elif not p[1].startswith('_'):
        var_handler.add_global_var(p[1], p.lineno(1))
    if not get_interpretation_state():
        set_interpretation_state(True)


def p_assignment_code(p):
    """
    assignment_code : definition EQUAL LBRACE
                    | variable EQUAL LBRACE
    """
    #  Make parser read the braced code without "simulating" execution
    set_interpretation_state(False)
    p[0] = p[1]


def p_arraydefinition(p):
    """
    arraydefinition : PRIVATE stringarray
    """
    print(*p)
    for index, element in enumerate(p[2]):
        element = element.replace('"', '')
        element = element.replace("'", "")
        if var_handler.has_local_var(element):
            print(f'ERROR: Local variable {element} already defined. Occurs on line: {p.lineno(1)}.', file=sys.stderr)
        else:
            if element[0] is not '_':
                print(f'ERROR: Attempt to declare global variable {element} as private on line: {p.lineno(1)}.', file=sys.stderr)
            if not element[1].islower():
                print(f'WARNING: Local variable {element} defined with unconventional casing on line: {p.lineno(1)}. '
                      f'Use lower case for the first character of local variables.', file=sys.stderr)
            var_handler.add_local_var(element, p.lineno(1))


def p_definition(p):
    """
    definition  : PRIVATE PRIVATE_ID
                | PRIVATE string
    """
    if p[2][0] in ['"', "'"]:
        p[2] = p[2].replace('"', '')
        p[2] = p[2].replace("'", "")
    if var_handler.has_local_var(p[2]):
        if get_interpretation_state:
            print(f'ERROR: Local variable {p[2]} already defined. Occurs on line: {p.lineno(1)}.', file=sys.stderr)
        p[0] = p[2]
    else:
        if not p[2][1].islower():
            print(f'WARNING: Local variable {p[2]} defined with unconventional casing. on line: {p.lineno(1)}. '
                  f'Use lower case for the first character of local variables.', file=sys.stderr)
        var_handler.add_local_var(p[2], p.lineno(1))
        p[0] = p[2]


def p_identifier(p):
    """
    identifier  : PRIVATE_ID %prec VARIABLE
                | GLOBAL_ID  %prec VARIABLE
    """
    if p[1].lower() in engine_functions:
        p[0] = p[1].lower()
    elif var_handler.has_local_var(p[1]):
        p[0] = var_handler.get_local_var(p[1])
    elif not p[1].startswith('_'):
        if var_handler.has_global_var(p[1]):
            p[0] = var_handler.get_global_var(p[1])
        else:
            var_handler.add_global_var(p[1], p.lineno(1))
            p[0] = p[1]
    else:
        if get_interpretation_state():
            print(f'ERROR: Undefined local variable {p[1]} used on line {p.lineno(1)}.', file=sys.stderr)
        p[0] = p[1]


def p_variable(p):
    """
    variable    : PRIVATE_ID %prec VARIABLE
                | GLOBAL_ID %prec VARIABLE
    """
    p[0] = p[1]


def p_binaryexp(p):
    """
    binaryexp   : primaryexp BINARY_FNC primaryexp          %prec BINARY_OP
                | primaryexp comparisonoperator primaryexp  %prec BINARY_OP
                | primaryexp mathoperator primaryexp        %prec BINARY_OP
    """


def p_primaryexp(p):
    """
    primaryexp  : number                    %prec VALUE
                | identifier                %prec VALUE
                | helpertype                %prec VALUE
                | unaryexp                  %prec UNARY_OP
                | nularexp                  %prec NULAR_OP
                | string                    %prec VALUE
                | binaryexp                 %prec BINARY_OP
                | bracedexp                 %prec BRACED_EXP
                | LPAREN binaryexp RPAREN   %prec BRACED_EXP
                | array                     %prec VALUE
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_bracedexp(p):
    """
    bracedexp : LBRACE new_scope code RBRACE
    """
    p[0] = p[3]
    pop_vars_and_warning_unused()


def p_new_scope(p):
    """new_scope :"""
    var_handler.new_local_scope()


def p_array(p):
    """
    array   : LSPAREN RSPAREN
            | LSPAREN arrayelement RSPAREN
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_arrayelement(p):
    """
    arrayelement    : binaryexp
                    | binaryexp COMMA arrayelement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[3], list):
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]] + [p[3]]


def p_stringarray(p):
    """
    stringarray : LSPAREN RSPAREN
                | LSPAREN stringarrayelement RSPAREN
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_stringarrayelement(p):
    """
    stringarrayelement  : string
                        | string COMMA stringarrayelement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[3], list):
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]] + [p[3]]



def p_nularexp(p):
    """
    nularexp    : NULAR_FNC     %prec NULAR_OP
                | identifier    %prec NULAR_OP
    """
    p[0] = p[1]
    

def p_unaryexp(p):
    """
    unaryexp    : UNARY_FNC primaryexp  %prec UNARY_OP
                | PLUS primaryexp       %prec UNARY_OP
                | MINUS primaryexp      %prec UNARY_OP
                | NOT primaryexp        %prec UNARY_OP
                | vardefinition         %prec UNARY_OP
    """


def p_comparisonoperator(p):
    """
    comparisonoperator  : LT            %prec COMPARISON_OP
                        | GT            %prec COMPARISON_OP
                        | LTE           %prec COMPARISON_OP
                        | GTE           %prec COMPARISON_OP
                        | EQUALITY      %prec COMPARISON_OP
                        | INEQUALITY    %prec COMPARISON_OP
                        | AND           %prec COMPARISON_OP
                        | OR            %prec COMPARISON_OP
    """
    p[0] = p[1]


def p_mathoperator(p):
    """
    mathoperator : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD
                    | POW
    """
    p[0] = p[1]


def p_booleanexp(p):
    """
    booleanexp  : primaryexp
                | primaryexp comparisonoperator booleanexp
                | primaryexp comparisonoperator LBRACE booleanexp RBRACE
    """


def p_configaccessor(p):
    """
    configaccessor  : GT GT     %prec CONFIG_ACCESSOR_GTGT
                    | DIVIDE    %prec CONFIG_ACCESSOR_SLASH
    """
    p[0] = ''.join(p[1:])


def p_number(p):
    """
    number  : NUMBER_REAL
            | NUMBER_EXP
            | NUMBER_HEX
    """
    p[0] = p[1]


def p_string(p):
    """
    string  : STRING_SINGLE
            | STRING_DOUBLE
    """
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    if p:
        print('ERROR: Unexpected "{}" on line:{}, pos:{}\n'.format(p.value, p.lineno, p.lexpos), file=sys.stderr)
    else:
        print('ERROR: File possibly contains an incomplete statement.\n', file=sys.stderr)


def get_interpretation_state():
    global is_interpreting
    return is_interpreting


def set_interpretation_state(state):
    global is_interpreting
    is_interpreting = state


def pop_vars_and_warning_unused():
    unused = var_handler.pop_local_stack()
    for name, var in unused.items():
        print(f'WARNING: Unused variable {name} declared on line: {var.declared_at}.', file=sys.stderr)


parser = pyacc.yacc()


def yacc():
    return parser
