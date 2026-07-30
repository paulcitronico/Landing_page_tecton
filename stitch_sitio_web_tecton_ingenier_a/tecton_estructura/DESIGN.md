---
name: Tecton Estructura
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#45474c'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
  outline: '#75777d'
  outline-variant: '#c5c6cd'
  surface-tint: '#555f71'
  primary: '#182232'
  on-primary: '#ffffff'
  primary-container: '#2d3748'
  on-primary-container: '#96a0b5'
  inverse-primary: '#bdc7dc'
  secondary: '#944b00'
  on-secondary: '#ffffff'
  secondary-container: '#fe9743'
  on-secondary-container: '#6b3500'
  tertiary: '#132235'
  on-tertiary: '#ffffff'
  tertiary-container: '#29384b'
  on-tertiary-container: '#92a1b8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e3f9'
  primary-fixed-dim: '#bdc7dc'
  on-primary-fixed: '#121c2c'
  on-primary-fixed-variant: '#3d4759'
  secondary-fixed: '#ffdcc5'
  secondary-fixed-dim: '#ffb783'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#703700'
  tertiary-fixed: '#d4e4fc'
  tertiary-fixed-dim: '#b8c8e0'
  on-tertiary-fixed: '#0d1c2e'
  on-tertiary-fixed-variant: '#39485c'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1280px
---

## Personalidad y Estilo
Este sistema de diseño proyecta la solidez, precisión y fiabilidad de la ingeniería civil moderna. El estilo es **Corporativo Moderno** con influencias geométricas, priorizando la claridad estructural y la legibilidad técnica. La experiencia visual debe evocar confianza absoluta, utilizando espacios amplios y alineaciones rigurosas que reflejen la exactitud de un plano arquitectónico. El objetivo es transmitir que cada píxel ha sido calculado con la misma integridad que una estructura de acero.

## Colores
La paleta se fundamenta en el contraste entre la estabilidad del sector industrial y la energía de la construcción activa.

- **Primario (Deep Slate):** Utilizado para navegación, encabezados y elementos estructurales. Representa el acero y la base sólida.
- **Secundario (Industrial Orange):** Reservado exclusivamente para llamadas a la acción (CTAs), estados activos y resaltados críticos. Evoca seguridad y visibilidad en obra.
- **Neutros:** Se utiliza una escala de grises fríos para fondos de contenedores y superficies, manteniendo la interfaz limpia y profesional.
- **Funcionales:** Verde para éxito en hitos de proyecto, Rojo para alertas de seguridad o errores técnicos.

## Tipografía
La jerarquía tipográfica equilibra el impacto visual con la funcionalidad técnica.

- **Encabezados (Montserrat):** Aportan un carácter geométrico y contundente. Se deben usar en pesos Bold o SemiBold para establecer una jerarquía clara.
- **Cuerpo de texto (Work Sans):** Elegida por su excelente legibilidad en informes técnicos y descripciones de proyectos. Su diseño optimizado para pantalla garantiza claridad en lecturas prolongadas.
- **Datos y Etiquetas (JetBrains Mono):** Se utiliza una fuente monoespaciada para valores numéricos, medidas y etiquetas de estado, reforzando la estética de precisión de ingeniería.

## Diseño y Espaciado
El sistema utiliza una **Cuadrícula Fija (Fixed Grid)** de 12 columnas para escritorio, asegurando que la información técnica esté siempre alineada y sea predecible.

- **Ritmo Vertical:** Basado en múltiplos de 8px para mantener la consistencia en formularios y tablas de datos.
- **Escritorio:** Margen lateral de 64px con medianiles (gutters) de 24px. Contenido centrado con un ancho máximo de 1280px.
- **Tablet:** Transición a una cuadrícula de 8 columnas con márgenes de 32px.
- **Móvil:** Cuadrícula de 4 columnas con márgenes de 16px. Los elementos apilables deben mantener un espaciado consistente de 16px o 24px para evitar la saturación visual.

## Elevación y Profundidad
La jerarquía se establece mediante **Sombras Ambientales** sutiles y capas tonales.

- **Nivel 0 (Base):** Fondos de página en `#F7FAFC`.
- **Nivel 1 (Tarjetas):** Superficies blancas con un borde fino de 1px en `#E2E8F0` y una sombra suave (`0 4px 6px -1px rgba(0,0,0,0.1)`).
- **Nivel 2 (Modales/Popovers):** Sombras más profundas y difusas para elevar elementos de interacción inmediata sobre el contenido principal.
- **Interacción:** Los elementos interactivos (botones) ganan una elevación ligera al pasar el cursor (hover), simulando una respuesta física al tacto.

## Formas
El lenguaje de formas es racional y moderado. Se utiliza un radio de esquina de **8px (Rounded)** para suavizar la dureza industrial sin perder la sensación de estructura y orden. 

- **Contenedores y Tarjetas:** Radio de 8px constante.
- **Botones:** Radio de 8px para mantener la coherencia con el sistema de cuadrícula.
- **Campos de Entrada:** Esquinas de 8px para proyectar modernidad y accesibilidad.

## Componentes

### Botones (Acciones)
- **Primario:** Fondo `#ED8936`, texto blanco, Montserrat Bold. Efecto de elevación sutil al hover.
- **Secundario:** Borde de 2px `#2D3748`, texto `#2D3748`, sin fondo. 
- **Terciario:** Solo texto con subrayado en hover, para acciones menos críticas.

### Campos de Entrada (Inputs)
- Fondo blanco, borde `#CBD5E0`, radio de 8px. 
- Al estar activo (focus), el borde cambia a `#ED8936` con un resplandor tenue.
- Las etiquetas (labels) siempre en `label-sm` usando JetBrains Mono para denotar precisión.

### Tarjetas de Proyecto (Cards)
- Estructura limpia con imagen superior.
- Título en `headline-md`.
- Uso de "Chips" o etiquetas con fondo gris claro para indicar categorías (ej. "Infraestructura", "Vivienda").

### Tablas de Datos
- Cabeceras en `#2D3748` con texto blanco.
- Filas con colores alternos muy sutiles para mejorar la lectura de planos y presupuestos.
- Alineación numérica a la derecha utilizando la fuente monoespaciada.

### Indicadores de Estado
- Píldoras con bordes redondeados al 100% (pill-shaped) para estados como "En Curso", "Finalizado" o "Pendiente de Revisión", utilizando colores semánticos suaves con texto de alto contraste.