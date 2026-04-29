---
name: Hospital Workflow Design System
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#3f484b'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#70797c'
  outline-variant: '#bfc8cb'
  surface-tint: '#1d6778'
  primary: '#004553'
  on-primary: '#ffffff'
  primary-container: '#0e5e6f'
  on-primary-container: '#94d5e9'
  inverse-primary: '#8fd0e4'
  secondary: '#006a63'
  on-secondary: '#ffffff'
  secondary-container: '#8bf1e6'
  on-secondary-container: '#006f67'
  tertiary: '#374041'
  on-tertiary: '#ffffff'
  tertiary-container: '#4e5758'
  on-tertiary-container: '#c4cdce'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#aeecff'
  primary-fixed-dim: '#8fd0e4'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5d'
  secondary-fixed: '#8ef4e9'
  secondary-fixed-dim: '#71d7cd'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#00504a'
  tertiary-fixed: '#dbe4e5'
  tertiary-fixed-dim: '#bfc8c9'
  on-tertiary-fixed: '#151d1e'
  on-tertiary-fixed-variant: '#404849'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: '0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 32px
  gutter: 24px
  section-gap: 48px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

The brand personality of the design system is anchored in empathy, precision, and tranquility. Designed for a high-stakes medical environment, it prioritizes a "calm-tech" approach to reduce the cognitive load on healthcare providers and the anxiety of patients. 

The aesthetic is **Corporate Modern** with a strong **Minimalist** influence. It avoids the coldness often associated with medical software by utilizing soft organic shapes and a breathable layout. Every visual decision is filtered through the lens of accessibility (WCAG 2.1 AA/AAA) and reassurance, ensuring that users feel supported by a reliable, human-centric interface.

## Colors

The palette is built on a foundation of trust and hygiene. The primary color is a deep, authoritative teal-blue that signifies expertise, while the secondary teal provides a softer, more calming secondary action color. 

- **Primary & Secondary:** Used for branding, primary actions, and navigational cues.
- **Surface Colors:** A range of very light cool-grays and whites are used to create "clinical" clarity without being sterile.
- **Semantic Colors:** Success, Warning, and Error colors are saturated but not jarring. They are always accompanied by icons or text labels to ensure accessibility for color-blind users.
- **Backgrounds:** Use the tertiary tint for large background areas to reduce screen glare during long shifts.

## Typography

This design system utilizes **Manrope** for its exceptional legibility and balanced geometric proportions. The typeface was chosen for its modern feel and its ability to remain readable even in dense data-heavy environments like patient charts.

- **Scale:** A generous scale is employed to ensure that critical information (like vitals or medication dosages) is never missed.
- **Hierarchy:** High-level headers use a tighter letter-spacing and heavier weights to anchor the page. 
- **Readability:** Body text uses a comfortable line height (1.5x - 1.6x) to allow for easier scanning of clinical notes.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with a strict 8px spacing system. This rhythm creates a sense of order and predictability across the application.

- **Grid:** A 12-column grid is used for desktop views, transitioning to a 4-column grid for mobile tablets.
- **Negative Space:** Whitespace is intentionally exaggerated between disparate sections to help patients and staff focus on one task at a time.
- **Information Density:** For clinician-facing dashboards, the "stack-sm" unit is used to increase density, while patient-facing portals utilize "stack-lg" to provide a more relaxed, approachable pace.

## Elevation & Depth

To convey hierarchy without overwhelming the user, the design system utilizes **Ambient Shadows** and **Tonal Layers**.

- **Depth Levels:** There are three distinct levels of elevation.
  1. **Base (0dp):** The main background surface, using the background neutral.
  2. **Flat (1dp):** Elements like input fields or static list items use a subtle 1px border (#E2E8F0) with no shadow.
  3. **Raised (2dp):** Interactive cards and modals use a soft, large-radius shadow with a low-opacity teal tint (`rgba(14, 94, 111, 0.08)`) to suggest a physical layer above the base.
- **Interaction:** Hover states slightly increase shadow spread to provide tactile feedback in a digital space.

## Shapes

The design system employs **Rounded** corners to evoke friendliness and safety. The use of sharp 90-degree angles is strictly avoided to minimize the "institutional" or "industrial" feel of the software.

- **Standard Components:** Buttons, cards, and input fields use a 0.5rem (8px) radius.
- **Large Components:** Modals and large content containers use a 1.5rem (24px) radius to create a distinct, containerized look.
- **Pills:** Status indicators (Tags/Chips) use a fully rounded (pill) shape to distinguish them from interactive buttons.

## Components

The components within this design system are built for high touch-accuracy and visual clarity.

- **Buttons:** Primary buttons are solid teal with white text; secondary buttons use a teal outline. All buttons have a minimum height of 48px to ensure ease of use on touch screens and for users with limited dexterity.
- **Cards:** Cards are the primary container for patient data. They feature a white background, a soft shadow, and a 2px colored "status accent" on the left border to indicate urgency at a glance.
- **Inputs:** Form fields use a soft-gray background to clearly define the hit area. Labels always sit above the field (never as placeholders) to maintain context during data entry.
- **Icons:** Use the custom "Friendly Outlined" set. Stroke weights are consistent (1.5px) and corners are slightly rounded to match the UI shape language.
- **Status Chips:** High-contrast background tints with darker text for maximum accessibility. (e.g., Success = Light Green BG + Dark Green Text).
- **Patient Progress Bar:** A custom component with a soft teal gradient and rounded caps to track recovery or workflow milestones in a non-threatening way.