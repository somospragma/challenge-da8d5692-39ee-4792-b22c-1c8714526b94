# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Consolidación de transacciones diarias en el modelo analítico**.

| | |
|---|---|
| Tema | pipelines de transformacion y carga |
| Nivel | advanced-l2 |
| Chapter | Ciencia de Datos — Ingeniero de Datos |
| Especialidad | Ingeniero de datos |
| Stack | Python 3.13 / PySpark 3.5.0 |
| Patron arquitectonico | ETL con etapas separadas y orquestación en Airflow |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `dags/ con el DAG de Airflow o el orquestador equivalente`
- `src/extract con los lectores de origen`
- `src/transform con las transformaciones y las reglas de calidad`
- `src/load con los escritores de destino`
- `tests/ con casos de validacion de resultados esperados`
- `conf/ con la configuracion por ambiente`

Dependencias:

- pyspark 3.5.0
- apache-airflow 2.9.2
- pandas 2.2.2
- pytest 8.1.1
- pydantic 2.7.1

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Exploración y modelado de datos**: Esquema de transacciones modeladas y reglas de calidad documentadas.
- **Fase 2 — Transformación de datos**: Proceso de transformación idempotente con reglas de calidad aplicadas y mecanismo de cuarentena para registros inválidos.
- **Fase 3 — Carga de datos en el modelo analítico**: Transacciones cargadas en el modelo analítico con idempotencia asegurada y registros inválidos en cuarentena.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Referencias colgando (1)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `requirements.txt` — `pyspark-sql@3.5.0`
      pyspark-sql declara la version 3.5.0, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.

### Presentes (13)

- `requirements.txt`
- `src/schemas/transacciones_schema.py`
- `dags/transacciones_etl_dag.py`
- `src/extract/extract_transacciones.py`
- `src/transform/transform_transacciones.py`
- `src/load/load_transacciones.py`
- `src/utils/quality_rules.py`
- `src/utils/idempotency_utils.py`
- `tests/test_extract_transacciones.py`
- `tests/test_transform_transacciones.py`
- `tests/test_load_transacciones.py`
- `conf/config_dev.json`
- `README.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `dags`
- `src/extract`
- `src/transform`
- `src/load`
- `src/schemas`
- `src/utils`
- `tests`
- `conf`
- `data/quarantine`
- `data/raw`
- `data/processed`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **ETL con etapas separadas y orquestación en Airflow**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Tecnología PySpark, Advanced
- Brecha que el reto ataca: Construye procesos de transformacion y carga idempotentes con reglas de calidad y cuarentena de registros invalidos
- Mision: Consolidar las transacciones diarias en el modelo analitico

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
