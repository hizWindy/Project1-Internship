import React from "react";
import { Flex, Box } from "@chakra-ui/react";
import { Outlet } from "react-router-dom";
import Navbar from "@/components/navbar"; // your custom navbar

const CompanyLayout = () => {
  return (
    <Flex direction="column" minHeight="100vh">
      {/* Navbar */}
      <Box as="header">
        <Navbar />
      </Box>

      {/* Main content */}
      <Box
        as="main"
        flex="1"             // makes main content grow to fill space
        px={{ base: 4, md: 8 }}  // responsive padding
        py={{ base: 6, md: 8 }}
     
        overflowX="hidden"   // prevent horizontal scroll
      >
        <Outlet />           {/* renders the pages */}
      </Box>

      {/* Optional footer */}
      <Box
        as="footer"
        bg="white"
        color="white"
        textAlign="center"
        px={{ base: 4, md: 8 }}
        py={4}
      >
        &copy; {new Date().getFullYear()} My Company
      </Box>
    </Flex>
  );
};

export default CompanyLayout;