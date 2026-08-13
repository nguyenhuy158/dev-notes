# .claudeignore

Repo nào cũng phải có file `.claudeignore` ở root.

Mục đích: chặn Claude Code đọc/ghi vào file/folder nhạy cảm hoặc không liên quan (secrets, `node_modules`, build output, file lớn không cần cho code review/agent).

Project mới: tạo `.claudeignore` ngay khi khởi tạo repo, không để agent tự động scan hết mọi thứ.

## Ví dụ — Cloudflare Worker (npm/pnpm)

```
node_modules/
dist/
.wrangler/
.dev.vars
.env
.env.*
*.log
pnpm-lock.yaml
package-lock.json
.git/
```

Ghi chú:
- `.dev.vars`, `.env*` — chứa secret (API key, DB token), không cho agent đọc.
- `.wrangler/`, `dist/` — build/cache output, không cần review.
- Lockfile (`pnpm-lock.yaml`, `package-lock.json`) — quá dài, không cần agent đọc trực tiếp, muốn xem dep thì check `package.json`.

