import React, { useState, useEffect } from "react"
import ResponsiveAppBar from "../components/appbar"
import { CssBaseline } from "@mui/material";

function Profile() {
    return (
        <div>
            <CssBaseline />
            <ResponsiveAppBar />
            <h2>"This is profile! (TO BE IMPLEMENT)"</h2>
        </div>
    );
}

export default Profile