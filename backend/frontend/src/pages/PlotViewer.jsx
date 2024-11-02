import React, { useState, useEffect } from "react"
import Plot from "../components/Plot"
import ResponsiveAppBar from "../components/appbar"
import Search from "../components/Search"
import { CssBaseline } from "@mui/material";
import api from "../api";
// import "../styles/PlotViewer.css"

function PlotViewer() {

    const [formData, setFormData] = useState({});
    const [plots, setPlots] = useState([]);

    const handleSubmit = (data) => {
        setFormData(data);
        fetchPlots(data);
    };

    const fetchPlots = (data) => {
        console.log('hello');
        api.get('http://127.0.0.1:8000/api/plot/', { params: data })
            .then(response => {
                console.log(response.data);
                setPlots(response.data);
            })
            .catch(error => {
                console.error('Error fetching plots:', error);
            });
    };

    return (
        <div>
            <ResponsiveAppBar />
            <CssBaseline />
            <Search onSubmit={handleSubmit} />
            <Plot plots={plots}/>
        </div>
    );
}

export default PlotViewer