# Consolidación de transacciones diarias en el modelo analítico

El sistema de procesamiento de datos de una institución financiera requiere consolidar transacciones diarias en el modelo analítico. Las transacciones provienen de múltiples fuentes (flujos de pago, movimientos de cuentas, transacciones de tarjeta) y deben ser transformadas y cargadas de manera idempotente. El objetivo es construir un proceso que asegure la calidad de los datos y coloque en cuarentena los registros inválidos.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | pipelines de transformacion y carga |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración y modelado de datos

**Objetivo:** Comprender la estructura y las reglas de las transacciones provenientes de las diferentes fuentes.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Analiza las fuentes de datos y sus respectivas estructuras.
- Identifica las reglas de calidad y las condiciones que deben cumplir las transacciones para ser consideradas válidas.
- Modela las transacciones en un esquema común para su posterior transformación.

**Entregable:** Esquema de transacciones modeladas y reglas de calidad documentadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la idempotencia en la modelación de datos.
- Piensa en cómo manejarías los registros inválidos.

</details>

### Fase 2: Transformación de datos

**Objetivo:** Transformar las transacciones de acuerdo a las reglas de calidad y asegurar la idempotencia del proceso.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Aplica las reglas de calidad identificadas en la fase anterior para transformar las transacciones.
- Asegura que el proceso de transformación sea idempotente.
- Implementa un mecanismo para colocar en cuarentena los registros inválidos.

**Entregable:** Proceso de transformación idempotente con reglas de calidad aplicadas y mecanismo de cuarentena para registros inválidos.

<details>
<summary>Pistas de conocimiento</summary>

- Reflexiona sobre cómo garantizar la idempotencia en cada paso de la transformación.
- Considera diferentes estrategias para manejar los registros inválidos.

</details>

### Fase 3: Carga de datos en el modelo analítico

**Objetivo:** Cargar las transacciones transformadas en el modelo analítico de manera idempotente.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Carga las transacciones transformadas en el modelo analítico.
- Asegura que el proceso de carga sea idempotente.
- Verifica que los registros inválidos estén correctamente en cuarentena.

**Entregable:** Transacciones cargadas en el modelo analítico con idempotencia asegurada y registros inválidos en cuarentena.

<details>
<summary>Pistas de conocimiento</summary>

- Reflexiona sobre cómo garantizar la idempotencia en el proceso de carga.
- Considera los impactos de los registros inválidos en el modelo analítico.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es la idempotencia en el contexto de la transformación y carga de datos?
- **paraQueSirve**: ¿Para qué sirve asegurar la idempotencia en el proceso de consolidación de transacciones?
- **comoSeUsa**: ¿Cómo se puede aplicar la idempotencia en la transformación y carga de datos?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar procesos idempotentes de transformación y carga de datos?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño de un proceso idempotente de transformación y carga de datos?

## Criterios de Evaluacion

- Implementar un proceso de transformación idempotente con reglas de calidad.
- Diseñar un mecanismo para colocar en cuarentena los registros inválidos.
- Asegurar la idempotencia en el proceso de carga de datos en el modelo analítico.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
