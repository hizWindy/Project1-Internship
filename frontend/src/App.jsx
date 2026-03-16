import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {
  Home,
  InternDashboard,
  InternApplications,
  Explore,
  Companies,
  CompaniesDashboard,
  Applicants,
  Postings,
  Interviews,
} from "./pages/index.js";
import InternLayout from "./layout/InternLayout.jsx";
import CompanyLayout from "./layout/CompanyLayout.jsx";

export default function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />

          <Route path="/interns" element={<InternLayout />}>
            <Route index element={<Explore />} />
            <Route path="dashboard" element={<InternDashboard />} />
            <Route
              path="intern-applications"
              element={<InternApplications />}
            />
            <Route path="companies" element={<Companies />} />
          </Route>

          <Route path="/companies" element={<CompanyLayout />}>
            <Route path="dashboard" index element={<CompaniesDashboard />} />
            <Route path="applicants" element={<Applicants />} />
            <Route path="postings" element={<Postings />} />
            <Route path="interviews" element={<Interviews />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}
