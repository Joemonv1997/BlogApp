import { useEffect } from "react";
import { createBrowserRouter, RouterProvider, useLoaderData } from "react-router-dom";
import { homePage } from "./common/loader";
import Error from "./Pages/error";
import Home from "./Pages/home";
function App() {
  return (
    <div>
      <h1>Welcome To Blog</h1>
      <RouterProvider router={router}></RouterProvider>
    </div>
  );
}

export default App;
const router=createBrowserRouter([
  {path:"/",element:<Home/>,loader:homePage,errorElement:<Error/>}
])