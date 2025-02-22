local total_experimentos = 1000000
local contador_eventos = 0
local examen = {}

for i = 1, 10 do
  examen[i] = math.random(3)
end

for i = 1, total_experimentos do
  local calificacion = 0
  for j = 1, #examen do
    if examen[j] == math.random(3) then
      calificacion = calificacion + 1
    end
  end
  if calificacion == 6 then
    contador_eventos = contador_eventos + 1
  end
end

print(contador_eventos / total_experimentos)
