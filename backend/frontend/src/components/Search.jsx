import { useEffect, useState } from 'react';
import axios from 'axios';

import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { Container, FormControl, Slider, Typography } from '@mui/material';
import regionFile from '../assets/region_List.txt';
import SubmitButton from '@mui/material/Button';
import Input from '@mui/material/Input';


const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// const get_region = async (regionList) => {
//     api.get('http://127.0.0.1:8000/api/plotcase/')
//         .then(response => {
//             setPlots(response.data);
//         })
//         .catch(error => {
//             console.error('Error fetching plots:', error);
//         });
// };

// const get_district = async (regionList) => {
//     try {
//         const response = await fetch(regionList);
//         const text = await response.text();
//         const lines = text.split('\n').map(line => line.trim()).filter(line => line !== '');
//         return lines;
//     } catch (error) {
//         console.error('Error reading region list:', error);
//         return [];
//     }
// };

// const get_sub_district = async (regionList) => {
//     try {
//         const response = await fetch(regionList);
//         const text = await response.text();
//         const lines = text.split('\n').map(line => line.trim()).filter(line => line !== '');
//         return lines;
//     } catch (error) {
//         console.error('Error reading region list:', error);
//         return [];
//     }
// };

const plotType = [
    {
        value: 'ทุกประเภท',
    },
    {
        value: 'ที่ดินว่างเปล่า',
    },
    {
        value: 'ห้องชุด',
    },
    {
        value: 'ที่ดินพร้อมสิ่งปลูกสร้าง',
    },
    {
        value: 'สิ่งปลูกสร้าง',
    },
];


const regionOptions = async () => {
    try {
        const response = await fetch(regionFile)
            .then(r => r.text())
        const lines = response.split('/').map(line => line.trim()).filter(line => line !== '');
        return lines;
    } catch (error) {
        console.error('Error reading region list:', error);
        return [];
    }
};

function valueLabelFormat(value) {
    const units = ['พัน บาท', 'หมื่น บาท', 'แสน บาท', 'ล้าน บาท'];
    const emptyUnit = '';

    let unitIndex = 0;
    let scaledValue = value;

    while (scaledValue >= 10 && unitIndex < units.length - 1) {
        unitIndex += 1;
        scaledValue /= 10;
    }

    if (value == 'max') {
        return `${scaledValue} ${emptyUnit}`;
    }
    else return `${scaledValue} ${units[unitIndex]}`;
}

function sizeLabelFormat(value) {
    const units = ['ตารางเมตร'];
    const emptyUnit = '';

    let unitIndex = 0;
    let scaledValue = value;

    // while (scaledValue >= 10 && unitIndex < units.length - 1) {
    //     unitIndex += 1;
    //     scaledValue /= 10;
    // }
    if (value == 'max') {
        return `${scaledValue} ${emptyUnit}`;
    }
    return `${scaledValue} ${units[unitIndex]}`;
}

function calculateValue(value) {
    if (value <= 10) {
        return value;
    } else if (value <= 29) {
        return 10 + (value - 10) * 10;
    } else if (value <= 47) {
        return 100 + (value - 28) * 100;
    }
    else if (value == 100) {
        return 'max'
    }
    else {
        return 1000 + (value - 46) * 1000;
    }
}

function calculateSize(value) {
    if (value <= 10) {
        return value;
    } else if (value <= 29) {
        return 10 + (value - 10) * 10;
    } else if (value <= 47) {
        return 100 + (value - 28) * 100;
    }
    else if (value == 100) {
        return 'max'
    }
    else {
        return 1000 + (value - 46) * 1000;
    }
}

function Search({ onSubmit }) {
    const [plotCases, setPlotCases] = useState([]);
    const [priceValue, setPriceValue] = useState([0, 100]);
    const [sizeValue, setSizeValue] = useState([0, 100]);
    const [provinces, setProvinces] = useState([]);
    const [selectedProvince, setSelectedProvince] = useState('');
    const [districtOptions, setDistrictOptions] = useState([]);
    const [subDistrictOptions, setSubDistrictOptions] = useState([]);
    const [selectedDistrict, setselectedDistrict] = useState('');
    const [selectedSubDistrict, setselectedSubDistrict] = useState('');
    const [selectedType, setSelectedType] = useState('ทุกประเภท');
    const [selectedSearch, setselectedSearch] = useState('');

    useEffect(() => {
        fetchPlotCases();
        loadRegions();
    }, []);

    useEffect(() => {
        updateDistrictAndSubDistrictOptions();
    }, [selectedProvince]);

    const handlePriceChange = (event, newValue) => {
        setPriceValue(newValue);
    }

    const handleSizeChange = (event, newValue) => {
        setSizeValue(newValue);
    }

    const fetchPlotCases = () => {
        api.get('http://127.0.0.1:8000/api/plotcase/')
            .then(response => {
                setPlotCases(response.data);
            })
            .catch(error => {
                console.error('Error fetching plots:', error);
            });
    };

    const loadRegions = async () => {
        const regionsList = await regionOptions();
        setProvinces(regionsList);
    };

    const updateDistrictAndSubDistrictOptions = () => {
        const filteredCases = plotCases.filter(plotCase => plotCase.case_province === " " + selectedProvince);
        const uniqueDistricts = [...new Set(filteredCases.map((x) => x.case_district))].sort();
        const uniqueSubDistricts = [...new Set(filteredCases.map((x) => x.case_sub_district))].sort();
        setDistrictOptions(uniqueDistricts);
        setSubDistrictOptions(uniqueSubDistricts);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const formData = {case_number: selectedSearch, case_province: selectedProvince, plot_type: selectedType, case_district: selectedDistrict, case_sub_district: selectedSubDistrict, valueMin: calculateValue(priceValue[0]) , valueMax: calculateValue(priceValue[1]), sizeMin: calculateSize(sizeValue[0]), sizeMax: calculateSize(sizeValue[1])};
        const test = {plot_type: selectedType};
        onSubmit(test);
    };

    //THE DISTRICT AND SUBDISTRICT SEEM TO BE MIXED UP. NEED TO SWAP THEM IN THE API. WILL TEMPORARY FIX HERE FOR NOW.

    return (
        <Container maxWidth={false} disableGutters>
            <FormControl
                sx={{
                    width: 1,
                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                }}
                noValidate
                autoComplete="off"
                onSubmit={handleSubmit}>

                <Box sx={{
                    width: 1,
                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                    padding: 5,
                }}>
                    <TextField id="outlined-search" label="เลขคดี" type="search" onChange={(event) => setselectedSearch(event.target.value)} />

                    <TextField
                        id="province-selector"
                        select
                        label="Select"
                        defaultValue=""
                        helperText="จังหวัด"
                        onChange={(event) => setSelectedProvince(event.target.value)}
                    >
                        {provinces.map((option) => (
                            <MenuItem key={option} value={option}>
                                {option}
                            </MenuItem>
                        ))}
                    </TextField>
                </Box>
                <Box sx={{
                    width: 1,
                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                    padding: 5,
                }}>
                    <TextField
                        id="district-selector"
                        select
                        label="Select"
                        defaultValue=""
                        helperText="อำเภอ"
                        onChange={(event) => setselectedDistrict(event.target.value)}
                    >
                        {subDistrictOptions.map((option) => (
                            <MenuItem key={option} value={option}>
                                {option}
                            </MenuItem>
                        ))}
                    </TextField>

                    <TextField
                        id="sub-district-selector"
                        select
                        label="Select"
                        defaultValue=""
                        helperText="ตำบล"
                        onChange={(event) => setselectedSubDistrict(event.target.value)}
                    >
                        {districtOptions.map((option) => (
                            <MenuItem key={option} value={option}>
                                {option}
                            </MenuItem>
                        ))}
                    </TextField>

                    <TextField
                        id="type-selector"
                        select
                        label="Select"
                        defaultValue="ทุกประเภท"
                        helperText="ประเภท"
                        onChange={(event) => setSelectedType(event.target.value)}
                    >
                        {plotType.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                                {option.value}
                            </MenuItem>
                        ))}
                    </TextField>
                </Box>
                <Box sx={{
                    width: 0.5,
                    alignItems: 'center',
                    padding: 5,
                }}>
                    <Typography id="price-slider" gutterBottom>
                        ราคา: {valueLabelFormat(calculateValue(priceValue[0]))} - {valueLabelFormat(calculateValue(priceValue[1]))}
                    </Typography>
                    <Slider
                        value={priceValue}
                        min={0}
                        step={1}
                        max={100}
                        scale={calculateValue}
                        getAriaValueText={valueLabelFormat}
                        valueLabelFormat={valueLabelFormat}
                        onChange={handlePriceChange}
                        valueLabelDisplay="auto"
                        aria-labelledby="price-slider"
                    />

                    <Typography id="size-slider" gutterBottom>
                        ขนาด: {sizeLabelFormat(calculateSize(sizeValue[0]))} - {sizeLabelFormat(calculateSize(sizeValue[1]))}
                    </Typography>
                    <Slider
                        value={sizeValue}
                        min={0}
                        step={1}
                        max={100}
                        scale={calculateSize}
                        getAriaValueText={sizeLabelFormat}
                        valueLabelFormat={sizeLabelFormat}
                        onChange={handleSizeChange}
                        valueLabelDisplay="auto"
                        aria-labelledby="size-slider"
                    />
                </Box>
                <Box sx={{
                    width: 0.2,
                    alignItems: 'right',
                    padding: 5,
                }}>
                    <SubmitButton sx={{ ml: 1 }} variant="contained" type="submit" onClick={handleSubmit}>
                        ค้นหา
                    </SubmitButton>
                </Box>
            </FormControl>
        </Container>
    );
}

export default Search;