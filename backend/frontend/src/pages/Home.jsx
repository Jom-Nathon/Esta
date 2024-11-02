import ResponsiveAppBar from "../components/appbar"

import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Hero from '../components/Hero';

function Home() {
    return (
        <div>
            <CssBaseline />
            <ResponsiveAppBar />
            <Hero />
            <Box sx={{ bgcolor: 'background.default' }}>
            </Box>
        </div>
    );
}

export default Home