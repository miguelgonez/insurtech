# Frontend React TypeScript - Sistema de Agentes Insurtech España

## Descripción

Este es el frontend moderno desarrollado en React con TypeScript para el Sistema de Agentes Insurtech España. Proporciona una interfaz de usuario intuitiva y responsive para interactuar con los agentes de IA especializados.

## Tecnologías Utilizadas

- **React 19** - Biblioteca de interfaz de usuario
- **TypeScript** - Tipado estático para JavaScript
- **Vite** - Herramienta de construcción y desarrollo
- **Tailwind CSS** - Framework de CSS utilitario
- **shadcn/ui** - Componentes de UI pre-construidos
- **Lucide React** - Iconos modernos
- **pnpm** - Gestor de paquetes

## Características

### 🏢 Consultas por Empresa
- Visualización de todas las empresas Insurtech españolas en tarjetas interactivas
- Selección intuitiva de empresas
- Formulario para realizar consultas específicas a agentes especializados
- Respuestas detalladas con formato mejorado

### 📊 Análisis Transversal
- Múltiples tipos de análisis disponibles
- Interfaz de selección visual para tipos de análisis
- Soporte para consultas personalizadas
- Resultados de análisis comparativo del ecosistema

### 🚀 Demo
- Demostración completa del sistema
- Ejecución de consultas de ejemplo
- Visualización de resultados de múltiples agentes

## Estructura del Proyecto

```
src/
├── components/
│   └── ui/           # Componentes de UI de shadcn
├── hooks/            # Hooks personalizados de React
├── lib/              # Utilidades y configuraciones
├── assets/           # Recursos estáticos
├── App.tsx           # Componente principal
├── main.tsx          # Punto de entrada
├── App.css           # Estilos específicos de la app
└── index.css         # Estilos globales
```

## Instalación y Desarrollo

### Prerrequisitos
- Node.js 18+
- pnpm (recomendado) o npm

### Instalación
```bash
cd insurtech-frontend
pnpm install
```

### Desarrollo
```bash
# Iniciar servidor de desarrollo
pnpm run dev

# Iniciar con acceso desde red
pnpm run dev --host
```

### Construcción para Producción
```bash
pnpm run build
```

### Vista Previa de Producción
```bash
pnpm run preview
```

## Configuración de API

El frontend está configurado para comunicarse con el backend Flask a través de un proxy en desarrollo:

```javascript
// vite.config.js
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true,
    }
  }
}
```

## Tipos TypeScript

El proyecto incluye tipos TypeScript bien definidos para:

- `Company` - Estructura de datos de empresas
- `CompanyQueryResponse` - Respuestas de consultas a empresas
- `AnalysisResponse` - Respuestas de análisis transversal
- `DemoResult` - Resultados de demostraciones

## Componentes Principales

### App.tsx
Componente principal que maneja:
- Estado global de la aplicación
- Comunicación con la API
- Navegación entre pestañas
- Manejo de errores y loading states

### Componentes UI
Utiliza componentes de shadcn/ui para:
- `Tabs` - Navegación por pestañas
- `Card` - Tarjetas de contenido
- `Button` - Botones interactivos
- `Input/Textarea` - Campos de formulario
- `Alert` - Mensajes de estado
- `Badge` - Etiquetas informativas

## Responsive Design

La interfaz está optimizada para:
- **Desktop** - Grid de 3 columnas para empresas
- **Tablet** - Grid de 2 columnas
- **Mobile** - Grid de 1 columna con navegación adaptada

## Características de UX

- **Loading States** - Indicadores de carga durante operaciones
- **Error Handling** - Manejo elegante de errores con alertas
- **Visual Feedback** - Estados hover y selección visual
- **Accessibility** - Componentes accesibles con shadcn/ui
- **Responsive** - Diseño adaptativo para todos los dispositivos

## Próximas Mejoras

- [ ] Implementar sistema de autenticación
- [ ] Agregar persistencia de estado con localStorage
- [ ] Implementar modo oscuro
- [ ] Agregar tests unitarios con Vitest
- [ ] Implementar lazy loading para mejor performance
- [ ] Agregar internacionalización (i18n)

