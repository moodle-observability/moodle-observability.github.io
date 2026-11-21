# Moodle Observability

Site institucional e portal hub de repositórios do ecossistema **Moodle Observability** no GitHub.

## 🌐 Internacionalização & Suporte Multilíngue
- **`/` (Root)**: Roteador com detecção automática do idioma do usuário (`navigator.language` / `localStorage`). Redireciona usuários em língua portuguesa para `/pt-br/` e aplica `/en/` como fallback (default).
- **`/en/`**: Versão completa em Inglês (default).
- **`/pt-br/`**: Versão completa em Português do Brasil.
- **Seletor no Header**: Ícones com as bandeiras dos EUA e do Brasil para alternância instantânea com persistência em `localStorage`.

O visual (`css/style.css`, `js/main.js`) é o mesmo do portal da [Moodle by KelsonCM](https://moodle-by-kelsoncm.github.io).

---

## 🗂️ Estrutura das Macro Seções (Grandes Cards)

1. **`🔌 Plugins Moodle`** (`#plugins`) — 5 repositórios, cada card com selo de status (Estável, Em desenvolvimento, Em pesquisa) e link para a documentação
   - **Rastreamento de Erros & APM** (`#error-tracking`): `moodle-tool_sentry`
   - **Métricas** (`#metrics`): `moodle-tool_prometheus`
   - **Cron & Tarefas** (`#tasks`): `moodle-tool_taskmonitor`
   - **Health Checks** (`#health`): `moodle-tool_healthcheck`
   - **Tracing** (`#tracing`): `moodle-tool_otel`

A documentação de cada plugin novo é publicada pelo próprio repositório em `https://moodle-observability.github.io/<repositório>/`.

Ficam fora do portal os repositórios internos (`.github`, `workspace`, `moodle-observability.github.io`).

Acesse o portal em: [https://moodle-observability.github.io](https://moodle-observability.github.io)
