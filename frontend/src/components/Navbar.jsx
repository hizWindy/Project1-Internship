import { Flex, Box, Button } from "@chakra-ui/react";

export default function Navbar() {
  return (
    <Flex
      as="nav"
      bg="white"
      color="black"
      px={6}
      py={4}
      justify="space-between"
      align="center"
    >
      <Box fontWeight="bold" fontSize="xl">
        My App
      </Box>
      <Flex gap={4}>
        <Button variant="solid">Home</Button>
        <Button variant="solid">Profile</Button>
        <Button variant="solid">Logout</Button>
      </Flex>
    </Flex>
  );
}
