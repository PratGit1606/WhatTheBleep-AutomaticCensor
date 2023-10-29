"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"


style = {
    "background_image" : "bg1.jpg",
    "#uploadText" :{
        "border" :  "2px solid rgb(128, 128, 128)",
        "width" : "200px",
        "height" : "160px",
        "font_family" : "Serif",
        "font_size" : "30px",
        "border_radius" : "15px",
        "position" : "absolute",
        "top" : "300px",
        "left" : "250px",
        "color" : "rgb(46, 162, 191)"
    },
    "#text1" :{
        "font_family" : "Serif",
    },
    "#words" : {
        "position" : "absolute",
        "top" : "630px",
        "left" : "125px",
        "border" : "2px solid rgb(128, 128, 128)",
        "bg" : "white",
        "width" : "500px",
        "height" : "100px",
        "font_size" : "20px"
    },
    "#inputButton" : {
        "position" : "absolute",
        "top" : "820px",
        "left" : "300px",
        "width" : "200px",
        "height" : "70px",
        "font_size" : "22px"
    },
    "#heading" : {
        "position" : "absolute",
        "top" : "760px",
        "left" : "130px",
    },
    "#display_video" : {
        "position" : "absolute",
        "top" : "400px",
        "left" : "10px",
        "width" : "100px",
        "height" : "40px"
    },
    "#UploadButton" : {
        "position" : "absolute",
        "top" : "400px",
        "left" : "320px",
        "width" : "150px",
        "height" : "70px"
    },
    "#vstackform" : {
        "position" : "absolute",
        "top" : "190px",
        "left" : "160px",
        "width" : "500px",
        "height" : "150px"
    },
    "#button1" : {
        "position" : "absolute",
        "top" : "40px",
        "left" : "130px",
    },
    "#ProcessButton" : {
        "background_color" : "lightgreen",
        "position" : "absolute",
        "top" : "440px",
        "left" : "830px",
        "width" : "160px",
        "height" : "80px",
        "font_size" : "25px"
    }


}
