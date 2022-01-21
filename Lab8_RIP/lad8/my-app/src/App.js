import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import DogeListPage from "./pages/DogeListPage";
import DogeDetailPage from "./pages/DogeDetailPage";

function App() {

  return (
      <BrowserRouter basename="/">
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/doge" element={<DogeListPage/>}/>
                <Route path="/doge/:pk" element={<DogeDetailPage/>}/>
            </Routes>
      </BrowserRouter>
  );
}
export default App;
