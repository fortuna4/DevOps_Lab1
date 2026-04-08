import sys
import os

# Добавляем путь к родительской папке, чтобы импортировать app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import_app():
    """Проверяет, что приложение импортируется без ошибок"""
    try:
        from app import app
        assert app is not None
        print("✓ Приложение импортируется корректно")
        return True
    except ImportError as e:
        print(f"✗ Ошибка импорта: {e}")
        return False

def test_convert_temperature():
    """Проверяет правильность конвертации температур"""
    from app import convert_temperature
    
    # Тестовые случаи: (значение, из_шкалы, в_шкалу, ожидаемый_результат)
    test_cases = [
        (0, "celsius", "fahrenheit", 32),
        (100, "celsius", "fahrenheit", 212),
        (0, "celsius", "kelvin", 273.15),
        (32, "fahrenheit", "celsius", 0),
        (212, "fahrenheit", "celsius", 100),
        (273.15, "kelvin", "celsius", 0),
        (0, "kelvin", "celsius", -273.15),
    ]
    
    all_passed = True
    for value, from_scale, to_scale, expected in test_cases:
        result = convert_temperature(value, from_scale, to_scale)
        # Округляем до 2 знаков для сравнения
        if round(result, 2) == round(expected, 2):
            print(f"✓ {value} {from_scale} → {to_scale} = {result}")
        else:
            print(f"✗ {value} {from_scale} → {to_scale}: ожидалось {expected}, получено {result}")
            all_passed = False
    
    return all_passed

def test_home_page():
    """Проверяет, что домашняя страница возвращает статус 200"""
    try:
        from app import app
        with app.test_client() as client:
            response = client.get('/')
            assert response.status_code == 200
            print("✓ Главная страница (/) работает")
            return True
    except Exception as e:
        print(f"✗ Ошибка при проверке главной страницы: {e}")
        return False

def test_convert_page_get():
    """Проверяет, что страница конвертации доступна"""
    try:
        from app import app
        with app.test_client() as client:
            response = client.get('/convert')
            assert response.status_code == 200
            print("✓ Страница конвертации (/convert) доступна")
            return True
    except Exception as e:
        print(f"✗ Ошибка при проверке страницы конвертации: {e}")
        return False

def test_convert_page_post():
    """Проверяет отправку POST-запроса на конвертацию"""
    try:
        from app import app
        with app.test_client() as client:
            response = client.post('/convert', data={
                'temperature': '100',
                'from_scale': 'celsius',
                'to_scale': 'fahrenheit'
            })
            assert response.status_code == 200
            # Проверяем, что результат 212 есть в ответе
            assert b'212' in response.data
            print("✓ POST-запрос на /convert работает корректно")
            return True
    except Exception as e:
        print(f"✗ Ошибка при POST-запросе: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Запуск тестов для приложения Temperature Converter")
    print("=" * 50)
    
    tests = [
        test_import_app,
        test_convert_temperature,
        test_home_page,
        test_convert_page_get,
        test_convert_page_post,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print()
        if test():
            passed += 1
    
    print()
    print("=" * 50)
    print(f"Результат: {passed}/{total} тестов пройдено")