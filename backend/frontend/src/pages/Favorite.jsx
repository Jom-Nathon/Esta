import React, { useState, useEffect } from "react"
import ResponsiveAppBar from "../components/appbar"
import { CssBaseline } from "@mui/material";
// import "../styles/Home.css"

function Favorite() {
    return (
        <div>
            <CssBaseline />
            <ResponsiveAppBar />
            <h2>"This is favorite (TO BE IMPLEMENT)"</h2>
        </div>
    );
}

export default Favorite