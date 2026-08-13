# Quy ước chung

## Package manager: pnpm

Luôn dùng **pnpm**, không dùng npm/yarn — kể cả khi thêm lib mới hay project
mới. Không tạo `package-lock.json`.

```
pnpm add <lib>
pnpm add -D <lib>
pnpm install
pnpm run <script>
```

Nếu project cũ đang có `package-lock.json`, đổi qua pnpm: xoá
`package-lock.json` + `node_modules`, chạy `pnpm import` (convert từ
package-lock) hoặc `pnpm install` thẳng nếu không cần giữ lockfile cũ.

## Kiến trúc: Hexagonal (Ports & Adapters)

Project mới nên tổ chức theo hexagonal architecture — tách domain/business
logic khỏi framework/IO. webhook-tester đã theo pattern này
(`src/adapters/inbound/http/...`), dùng làm mẫu tham khảo.

Cấu trúc gợi ý:

```
src/
  domain/           # entity, business rule thuần, không import framework
  ports/            # interface domain cần (repository, notifier...)
  adapters/
    inbound/        # HTTP handler, CLI, cron trigger — gọi vào domain
    outbound/       # DB (Drizzle/D1), email, third-party API — implement ports
```

Domain không import trực tiếp Hono/D1/React — chỉ định nghĩa qua `ports/`,
adapter nào cũng thay được (đổi DB, đổi framework HTTP) mà không sửa domain.

Project nhỏ/1-file-script không cần áp dụng cứng, ưu tiên cho app có logic
nghiệp vụ thật (chia-keo, cardstat, sso...).
