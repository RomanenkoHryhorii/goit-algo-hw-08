import heapq

def minimize_cable_connection_cost(cable_lengths):
    """
    Знаходження мінімальної вартості з'єднання кабелів.
    
    :param cable_lengths: Список довжин кабелів
    :return: Мінімальна загальна вартість з'єднання кабелів
    """
    # Перетворюємо список на купу
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Продовжуємо з'єднання, поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Vitягуємо два найкоротших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Обчислюємо вартість з'єднання
        connection_cost = first + second
        total_cost += connection_cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cable_lengths, connection_cost)
    
    return total_cost

# Приклад використання
cables = [5, 2, 7, 3]
min_cost = minimize_cable_connection_cost(cables)
print(f"Мінімальна вартість з'єднання кабелів: {min_cost}")