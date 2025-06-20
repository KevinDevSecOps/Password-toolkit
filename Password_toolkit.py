import secrets
import string
import hashlib
import requests
from argparse import ArgumentParser

# Configuración
class PasswordToolkit:
    def __init__(self):
        self.common_passwords_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
    
    def generar_contraseña(self, longitud=12, usar_simbolos=True, usar_mayusculas=True, usar_numeros=True):
        """Genera una contraseña segura con criterios personalizables."""
        caracteres = string.ascii_lowercase
        if usar_mayusculas:
            caracteres += string.ascii_uppercase
        if usar_numeros:
            caracteres += string.digits
        if usar_simbolos:
            caracteres += string.punctuation
        
        if not caracteres:
            raise ValueError("Debes habilitar al menos un tipo de carácter.")
        
        return ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    def es_contraseña_fuerte(self, contraseña, min_longitud=12, verificar_comun=True):
        """Valida la fortaleza de una contraseña."""
        if len(contraseña) < min_longitud:
            return False, f"❌ Longitud mínima no alcanzada ({min_longitud} caracteres)."
        
        tiene_mayusculas = any(c.isupper() for c in contraseña)
        tiene_numeros = any(c.isdigit() for c in contraseña)
        tiene_simbolos = any(c in string.punctuation for c in contraseña)
        
        if not (tiene_mayusculas and tiene_numeros and tiene_simbolos):
            return False, "❌ Faltan mayúsculas, números o símbolos."
        
        if verificar_comun and self.es_contraseña_comun(contraseña):
            return False, "❌ La contraseña está en listas de contraseñas comunes."
        
        return True, "✅ Contraseña segura."
    
    def es_contraseña_comun(self, contraseña):
        """Verifica si la contraseña está en listas de contraseñas vulneradas."""
        try:
            response = requests.get(self.common_passwords_url, timeout=5)
            common_passwords = response.text.splitlines()
            return contraseña in common_passwords
        except requests.RequestException:
            return False
    
    def hash_contraseña(self, contraseña, algoritmo='sha256'):
        """Genera el hash de una contraseña (útil para almacenamiento seguro)."""
        return hashlib.new(algoritmo, contraseña.encode()).hexdigest()

# CLI
def main():
    parser = ArgumentParser(description="🔐 Generador y Validador de Contraseñas Seguras")
    parser.add_argument("--generar", action="store_true", help="Genera una contraseña segura.")
    parser.add_argument("--validar", type=str, help="Valida la fortaleza de una contraseña.")
    parser.add_argument("--longitud", type=int, default=12, help="Longitud de la contraseña (default: 12).")
    parser.add_argument("--simbolos", action="store_true", help="Incluye símbolos en la contraseña.")
    args = parser.parse_args()
    
    toolkit = PasswordToolkit()
    
    if args.generar:
        contraseña = toolkit.generar_contraseña(
            longitud=args.longitud,
            usar_simbolos=args.simbolos
        )
        print(f"🔒 Contraseña generada: {contraseña}")
        print(f"🔑 Hash (SHA-256): {toolkit.hash_contraseña(contraseña)}")
    elif args.validar:
        es_segura, mensaje = toolkit.es_contraseña_fuerte(args.validar)
        print(mensaje)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
