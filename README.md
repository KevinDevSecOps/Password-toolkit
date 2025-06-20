# 🛡️ **SecurePass Generator** - by KevinDevSecOps
*Genera contraseñas seguras y valida su fortaleza en segundos*
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)  

---

## 📌 **Descripción**  
Herramienta CLI en Python para:  
✅ **Generar** contraseñas aleatorias con criterios personalizables.  
✅ **Validar** si una contraseña es resistente a ataques (brute force, diccionario, etc.).  
✅ **Educar** sobre buenas prácticas de seguridad.  

---

## 🛠️ **Instalación**  
1. Clona el repositorio:  
   ```bash
   git clone https://github.com/KevinDevSecOps/password-toolkit.git
   ```
2. Instala dependencias:  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 **Uso**  
### 🔧 **Generar contraseña**  
```bash
python password_toolkit.py --generar --longitud 16 --simbolos
```  
**Opciones**:  
- `--longitud`: Longitud de la contraseña (default: 12).  
- `--simbolos`: Incluye caracteres especiales (@, !, etc.).  

### 🔍 **Validar contraseña**  
```bash
python password_toolkit.py --validar "MiContraseña123!"
```  
**Salida**:  
```
✅ Fortaleza: Alta (longitud: 15, tiene mayúsculas, números y símbolos).
❌ No usar palabras comunes (evita "Contraseña").
```

---

## ⚙️ **Tecnologías**  
- Python 3.8+  
- Librerías: `secrets`, `hashlib`, `string`  
- Integración con [Have I Been Pwned? API](https://haveibeenpwned.com/API/v3) (opcional).  

---

## 📂 **Estructura del Proyecto**  
```
password-toolkit/
├── src/
│   ├── password_toolkit.py  # Lógica principal
│   ├── wordlists/           # Diccionarios para evitar (ej: rockyou.txt)
├── tests/                   # Tests unitarios
├── requirements.txt         # Dependencias
└── README.md                # Este archivo
```

---

## 📜 **Licencia**  
MIT License - Copyright (c) 2024 [KevinDevSecOps](https://github.com/KevinDevSecOps).  

---

## 🤝 **Contribuciones**  
¡Se aceptan PRs! Antes de contribuir:  
1. Abre un **Issue** describiendo el cambio.  
2. Haz un **Fork** y envía un Pull Request.  

---

## 🌟 **Ejemplo en Acción**  
```python
from password_toolkit import generar_contraseña

print(generar_contraseña(longitud=14, simbolos=True))
# Salida: "xQ3!k9@L$vB2#N"
```

---

Hecho con ❤️ por [KevinDevSecOps](https://github.com/KevinDevSecOps).  
