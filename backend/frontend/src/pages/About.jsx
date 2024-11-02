import React, { useState, useEffect } from "react"
import api from "../api"
import Plot from "../components/Plot"
import { CssBaseline } from "@mui/material"
import ResponsiveAppBar from "../components/appbar"

function About() {

    return (
        <div>
            <CssBaseline />
            <ResponsiveAppBar />

            <h2>
                About
            </h2>
        </div>
    );
}

export default About