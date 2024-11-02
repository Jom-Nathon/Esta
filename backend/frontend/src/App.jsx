import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import NotePage from './pages/NotePage'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import PlotViewer from './pages/PlotViewer'
import About from './pages/About'
import Profile from './pages/Profile'
import Favorite from './pages/Favorite'
import ProtectedRoute from './components/ProtectedRoute'

function Logout() {
  localStorage.clear()
  return <Navigate to='/login' />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path='/plotviewer'
          element={
            <ProtectedRoute>
              <PlotViewer />
            </ProtectedRoute>
          }
        />
        <Route
          path='/note'
          element={
            <ProtectedRoute>
              <NotePage />
            </ProtectedRoute>
          }
        />
        <Route path='/login' element={<Login />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/register' element={<RegisterAndLogout />} />
        <Route path='/about' element={<About />} />
        <Route path='/profile' element={<Profile />} />
        <Route path='/favorite' element={<Favorite />} />
        <Route path='/' element={<ProtectedRoute><Home/></ProtectedRoute>}/>
        <Route path='*' element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
