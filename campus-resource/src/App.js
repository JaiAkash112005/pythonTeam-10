import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import UserList from "./pages/users/UserList";
import AddUser from "./pages/users/AddUser";
import ResourceList from "./pages/resources/ResourceList";
import AddResource from "./pages/resources/AddResource";
import BookingList from "./pages/bookings/BookingList";
import AddBooking from "./pages/bookings/AddBooking";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/add-user" element={<AddUser />} />
        <Route path="/resources" element={<ResourceList />} />
        <Route path="/add-resource" element={<AddResource />} />
        <Route path="/bookings" element={<BookingList />} />
        <Route path="/add-booking" element={<AddBooking />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
