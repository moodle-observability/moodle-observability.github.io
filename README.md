# Moodle Observability

Site institucional e portal hub de repositórios do ecossistema **Moodle Observability** no GitHub.

## 🌐 Internacionalização & Suporte Multilíngue
- **`/` (Root)**: Roteador com detecção automática do idioma do usuário (`navigator.language` / `localStorage`). Redireciona usuários em língua portuguesa para `/pt-br/` e aplica `/en/` como fallback (default).
- **`/en/`**: Versão completa em Inglês (default).
- **`/pt-br/`**: Versão completa em Português do Brasil.
- **Seletor no Header**: Ícones com as bandeiras dos EUA e do Brasil para alternância instantânea com persistência em `localStorage`.

O visual (`css/style.css`, `js/main.js`) é o mesmo do portal da [Moodle by KelsonCM](https://moodle-by-kelsoncm.github.io).


## 🎨 Identidade visual

Logo da organização (quadrada, sem cantos arredondados: cada aplicação arredonda como quiser): monograma **"o11"** (o "o" e o "11" de *mo11y*: anel laranja `#ea580c` e duas barras de métrica, laranja e azul `#0284c7`).

| Arquivo | Uso |
| :--- | :--- |
| `img/logo.svg` | Logo quadrada com fundo branco, sem cantos arredondados (favicon SVG e uso geral) |
| `img/logo-mark.svg` | Só o símbolo, fundo transparente (cabeçalho do portal) |
| `img/logo-512.png` | PNG 512 px (`og:image` e avatar da organização no GitHub) |
| `img/apple-touch-icon.png` | Ícone 180 px para iOS |
| `favicon.ico` | Favicon 16/32/48 px |


---

## 🗂️ Estrutura das Macro Seções (Grandes Cards)

1. **`🔌 Plugins Moodle`** (`#plugins`) — 5 repositórios numa grade única (sem subcategorias, já que cada categoria teria um só plugin). A categoria aparece como primeira tag do card, que também traz o selo de status (Estável, Em desenvolvimento, Em pesquisa) e o link para a documentação:
   - `moodle-tool_sentry` — Rastreamento de Erros & APM
   - `moodle-tool_prometheus` — Métricas
   - `moodle-tool_taskmonitor` — Cron & Tarefas
   - `moodle-tool_healthcheck` — Health Checks
   - `moodle-tool_otel` — Tracing

A documentação de cada plugin novo é publicada pelo próprio repositório em `https://moodle-observability.github.io/<repositório>/`.

Ficam fora do portal os repositórios internos (`.github`, `workspace`, `moodle-observability.github.io`).

Acesse o portal em: [https://moodle-observability.github.io](https://moodle-observability.github.io)
