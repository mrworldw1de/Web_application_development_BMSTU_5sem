import {Link} from "react-router-dom";
import {Navbar, Nav, Container} from "react-bootstrap";

function Header() {
    return (
        <Navbar bg="dark blue" variant="">
            <Container>
                <Navbar.Brand as={Link} to="/">Лаб 8</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link as={Link} to="/">Главная</Nav.Link>
                    <Nav.Link as={Link} to="/Doge/">Собаки</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );
}

export default Header;