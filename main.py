from pprint import pprint  # импорт модуля pprint для красивого вывода


class RoadTrafficSimulation:

  def __init__(self, road, n):
    self.road = road
    self.n = n
    self.signals = ["G", "O", "R"]
    self.signal_cycle = [5, 1, 5]

  def simulate(self):
    result = [self.road]

    for i in range(self.n):
      new_road = list(result[i])
      j = -1  # переменная цикла для while
      c_ind = new_road.index("C")  # текущий индекс машины
      # поменяли for на while и добавили отдельный индекс для машины
      # т.к. если использовать for, то он каждый раз стирает следующую машину
      while j < len(new_road):
        j += 1
        if c_ind == len(new_road) - 1:
          break
        # если следующий индекс после C = .
        if new_road[c_ind + 1] == ".":
          new_road[c_ind] = "."
          new_road[c_ind + 1] = "C"
        # если следующий индекс после C = R
        elif new_road[c_ind + 1] == "R":
          new_road[c_ind] = "."
          new_road[c_ind + 1] = "C"
        # если следующий индекс после C = O
        elif new_road[c_ind + 1] == "O":
          new_road[c_ind] = "."
          new_road[c_ind + 1] = "C"
        # если следующий индекс после C = G
        elif new_road[c_ind + 1] == "G":
          new_road[c_ind] = "."
          new_road[c_ind + 1] = "C"

        # разобрались со светофорами
        if new_road[(j + 1) % len(new_road)] in self.signals:
          new_road[(j + 1) %
                   len(new_road)] = self.signals[(i // sum(self.signal_cycle))
                                                 % len(self.signals)]

      result.append("".join(new_road))

    return result


# road = "C................."  # пустая дорога
road = "C...R...R.R..G....G"  # дорога со светофорами
n = 15
simulation = RoadTrafficSimulation(road, n)
result = simulation.simulate()
pprint(result)  # добавили pprint чтобы результат был в колонку
