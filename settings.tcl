#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 594x400+100+0
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1916 1053
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "photobooth settings"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command onBtnSaveConfig \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font11,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Save 
    vTcl:DefineAlias "$top.but45" "btnSave" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa48 \
        -background {#d9d9d9} -foreground {#000000} -relief flat \
        -justify right -text {Print style:} 
    vTcl:DefineAlias "$top.tLa48" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo49 \
        -textvariable combobox -foreground {} -background {} -takefocus {} \
        -cursor arrow 
    vTcl:DefineAlias "$top.tCo49" "cbPrintFormat" vTcl:WidgetProc "Toplevel1" 1
    button $top.but37 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command onBtnCameraUpdate \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Update 
    vTcl:DefineAlias "$top.but37" "btnCameraUpdate" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Delay screens:} 
    vTcl:DefineAlias "$top.lab40" "Label5" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo43 \
        -textvariable combobox2 -foreground {} -background {} -takefocus {} \
        -cursor arrow 
    vTcl:DefineAlias "$top.tCo43" "cbDelayScreen" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa44 \
        -background {#d9d9d9} -foreground {#000000} -relief flat \
        -text {'Strike a pose' delay:} 
    vTcl:DefineAlias "$top.tLa44" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.tEn45 \
        -textvariable txtSAPVar -foreground {} -background {} -takefocus {} \
        -cursor arrow 
    vTcl:DefineAlias "$top.tEn45" "txtSAP" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa46 \
        -background {#d9d9d9} -foreground {#000000} -relief flat -text ms 
    vTcl:DefineAlias "$top.tLa46" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
    canvas $top.can51 \
        -background white -borderwidth 2 -closeenough 1.0 -height 153 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 186 
    vTcl:DefineAlias "$top.can51" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command onBtnTakePhoto \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Take photo} 
    vTcl:DefineAlias "$top.but52" "btnTakePhoto" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Camera: 
    vTcl:DefineAlias "$top.cpd54" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify right -text Printer: -width 54 
    vTcl:DefineAlias "$top.cpd56" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -textvariable lblCameraVar 
    vTcl:DefineAlias "$top.cpd57" "lblCamera" vTcl:WidgetProc "Toplevel1" 1
    label $top.cpd58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffffff} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -textvariable lblPrinterVar 
    vTcl:DefineAlias "$top.cpd58" "lblPrinter" vTcl:WidgetProc "Toplevel1" 1
    button $top.cpd59 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command onBtnPrinterUpdate \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Update 
    vTcl:DefineAlias "$top.cpd59" "btnUpdatePrinter" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che61 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify left -text {Preview screen} \
        -variable ckBoxVar 
    vTcl:DefineAlias "$top.che61" "ckPreviewScreen" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {End screen delay:} 
    vTcl:DefineAlias "$top.lab62" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Preview screen delay:} 
    vTcl:DefineAlias "$top.lab63" "Label7" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.cpd64 \
        -textvariable txtEndScreenDelayVar -foreground {} -background {} \
        -takefocus {} -cursor arrow 
    vTcl:DefineAlias "$top.cpd64" "txtEndDelay" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.cpd65 \
        -textvariable txtPreviewScreenDelay -foreground {} -background {} \
        -takefocus {} -cursor arrow 
    vTcl:DefineAlias "$top.cpd65" "txtPreviewDelay" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.cpd37 \
        -background {#d9d9d9} -foreground {#000000} -relief flat -text ms 
    vTcl:DefineAlias "$top.cpd37" "TLabel4" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.cpd38 \
        -background {#d9d9d9} -foreground {#000000} -relief flat -text ms 
    vTcl:DefineAlias "$top.cpd38" "TLabel5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command onPreviewPrintStyle \
        -disabledforeground {#a3a3a3} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Preview 
    vTcl:DefineAlias "$top.but39" "btnPreviewPrintStyle" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.cpd40 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -justify left -offvalue False -onvalue True \
        -text {Show mouse} -variable ckShowMouseVar -width 101 
    vTcl:DefineAlias "$top.cpd40" "ckShowMouse" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab37 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} \
        -text {If preview screen delay set to 0 then continue by tap} \
        -wraplength 200 
    vTcl:DefineAlias "$top.lab37" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 440 -y 330 -width 127 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa48 \
        -in $top -x 68 -y 113 -width 61 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo49 \
        -in $top -x 140 -y 114 -width 124 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but37 \
        -in $top -x 510 -y 8 -width 67 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab40 \
        -in $top -x 44 -y 145 -width 90 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo43 \
        -in $top -x 140 -y 146 -width 124 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa44 \
        -in $top -x 20 -y 176 -width 110 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tEn45 \
        -in $top -x 140 -y 176 -width 84 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa46 \
        -in $top -x 227 -y 178 -width 20 -height 19 -anchor nw \
        -bordermode ignore 
    place $top.can51 \
        -in $top -x 20 -y 210 -width 186 -relwidth 0 -height 153 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 20 -y 370 -width 187 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd54 \
        -in $top -x 0 -y 10 -width 64 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode inside 
    place $top.cpd56 \
        -in $top -x 8 -y 40 -width 54 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd57 \
        -in $top -x 81 -y 10 -width 424 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.cpd58 \
        -in $top -x 81 -y 40 -width 424 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.cpd59 \
        -in $top -x 510 -y 38 -width 67 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che61 \
        -in $top -x 410 -y 90 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 322 -y 142 -width 117 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab63 \
        -in $top -x 312 -y 169 -width 118 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd64 \
        -in $top -x 438 -y 142 -width 64 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.cpd65 \
        -in $top -x 438 -y 169 -width 64 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.cpd37 \
        -in $top -x 506 -y 170 -width 20 -height 19 -anchor nw \
        -bordermode ignore 
    place $top.cpd38 \
        -in $top -x 506 -y 143 -width 20 -height 19 -anchor nw \
        -bordermode ignore 
    place $top.but39 \
        -in $top -x 270 -y 112 -width 57 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cpd40 \
        -in $top -x 410 -y 110 -width 101 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab37 \
        -in $top -x 302 -y 190 -width 214 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37

