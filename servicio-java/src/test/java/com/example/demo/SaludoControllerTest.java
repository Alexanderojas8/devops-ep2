package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class SaludoControllerTest {

    private final SaludoController controller = new SaludoController();

    @Test
    void saludoRetornaTexto() {
        assertEquals("Hola desde Java", controller.saludo());
    }

    @Test
    void sumarDosNumeros() {
        assertEquals(5, controller.sumar(2, 3));
    }
}