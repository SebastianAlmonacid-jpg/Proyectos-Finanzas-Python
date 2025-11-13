# Proyectos-Finanzas-y-Python
Proyectos de Análisis de Inversiones con Python: Modelos, Riesgo y Optimización.

# Sebastián Ricardo Almonacid Riquelme
### Ingeniero Civil Industrial | Análisis y Modelación Financiera con Python

Bienvenido a mi portafolio. Soy Ingeniero Civil Industrial y he desarrollado esta colección de proyectos como un **estudio autodidacta enfocado** para construir las habilidades técnicas y de dominio necesarias para una carrera en la banca de inversión.

Mi formación en ingeniería se centra en la optimización de procesos y el análisis de sistemas. Este portafolio es la aplicación de esa mentalidad de resolución de problemas para:

1.  **Dominar las herramientas de software** (`Python`).
2.  **Aprender y aplicar los modelos financieros** (`CAPM`, `Optimización de Portafolios`, `Valoración FCD`, `Valoración de opciones Europeas`').

Mi objetivo es demostrar mi capacidad de aprender y ejecutar análisis complejos, y mi compromiso para entrar en el entorno de la banca de inversión.

* **Email:** `[salmonacid@alumnos.uai.cl]`

---

### Stack Tecnológico 

* **Lenguaje Utilizado:** `Python`
* **Análisis y Modelación:** `Pandas`, `NumPy`, `Statsmodels (OLS)`, `SciPy (Optimize)`
* **Visualización de Datos:** `Matplotlib`, `Seaborn`, `Plotly`
* **Fuentes de Datos:** `yfinance`
  
### Análisis Conceptual y Financiero

* **Análisis de Datos y Visualización (EDA):** Limpieza, manipulación y exploración gráfica de datos
* **Teoría de Portafolio y Riesgo (CAPM):** Cálculo de Beta, Alpha, VaR, CVaR, análisis de riesgo sistemático y backtesting condicional de Alpha.
* **Valoración de Derivados:** Cálculo del precio teórico de Opciones Europeas (Call/Put) usando **GBM** (Modelo Black-Scholes).
* **Optimización de Portafolios:** Creación de la Frontera Eficiente, Simulación de Monte Carlo y maximización del **Ratio de Sharpe** (`SciPy`).
* **Valoración de Empresas (Corporate Finance):** Proyección de flujos de caja y valoración por **FCD** con Monte Carlo.

---

### Proyectos del Portafolio

1.  **Fundamentos de Análisis de Datos (EDA y Visualización)**
2.  **Análisis de Riesgo (CAPM) y Backtesting de Alpha**
3.  **Valoración de Derivados (Opciones Black-Scholes)**
4.  **Optimización de Portafolios (Frontera Eficiente y CAL)**
5.  **Valoración de Empresas (FCD con Monte Carlo)**

---

### Detalle de Proyectos

#### 1. Fundamentos de Análisis de Datos (EDA)
* **Objetivo:** Mostrar la capapacidad de limpieza, manipulación (`pandas`) y visualización (`matplotlib`, `seaborn`, `plotly`) de un conjunto de datos de empleados.
* **Metodología:** El proyecto consistió en la limpieza de datos, cálculo y adición de columnas y una **validación crítica** de los mismos. Posteriormente, se realizó una exploración visual para analizar distribuciones y relaciones en los datos.

#### 2. Análisis de Riesgo (CAPM) y Backtesting de Alpha
* **Objetivo:** Determinar el riesgo sistemático (**Beta**) y la Línea de Mercado (SML) usando CAPM, y subsecuentemente **investigar la discrepancia** entre el retorno esperado por el modelo y el retorno aritmético promedio.
* **Metodología:** Se ejecutó un CAPM general (obteniendo **Beta** y un **Alpha no significativo**), revelando una gran discrepancia con el retorno aritmético promedio. Para explicar esto, se implementó un **backtest condicional** (8 señales, ej. RSI) que **encontró el Alpha estadísticamente significativo**  (`p-value ≈ 0`) que el modelo general no pudo ver. Este Alpha provenía de condiciones específicas: `RSI > 70` (Activo) y `RSI > 70` + `Precio M > MM200` (Cartera).

#### 3. Valoración de Derivados (Opciones Black-Scholes)
* **Objetivo:** Calcular el precio teórico y las "Griegas" de Opciones Europeas (Call y Put).
* **Metodología:** Implementación del modelo Black-Scholes utilizando una simulación de **Movimiento Geométrico Browniano (GBM)** para proyectar el precio del subyacente.
  
#### 4. Optimización de Portafolios (Frontera Eficiente y CAL)
* **Objetivo:** Construir la Frontera Eficiente para encontrar la cartera de **Máximo Ratio de Sharpe** y la de **Mínima Volatilidad Global**, concluyendo con el desarrollo de la Línea de Asignación de Capital (CAL).
* **Metodología:** Uso de **Simulación Monte Carlo** (para explorar) y el optimizador **`SciPy SLSQP`** (para el cálculo preciso de los pesos) y la posterior derivación de la CAL.

#### 5. Valoración de Empresas (FCD con Monte Carlo)
* **Objetivo:** Proyectar el valor de una empresa mediante un modelo FCD y aplicar una simulación de Monte Carlo para medir el riesgo de la valoración.
* **Metodología:** Proyección de *drivers* usando **GBM** (para Ventas) y **Reversión a la Media (ABM)** (para ratios), seguido del descuento de flujos de caja.
