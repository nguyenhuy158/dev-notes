# Xử lý ngày tháng: date-fns

Chưa dùng project nào. Dùng khi cần format/tính toán ngày (deadline chia
tiền, lịch, "3 ngày trước") thay vì tự viết bằng `Date` thuần hoặc kéo
`moment.js` (nặng, deprecated).

```
pnpm add date-fns
```

```ts
import { format, formatDistanceToNow, addDays } from "date-fns";
import { vi } from "date-fns/locale";

format(new Date(), "dd/MM/yyyy", { locale: vi }); // "10/08/2026"
formatDistanceToNow(deadline, { locale: vi, addSuffix: true }); // "3 ngày trước"
addDays(new Date(), 7);
```

Import theo function (`date-fns/xxx` hoặc named import từ `date-fns` bản
v3+) — tree-shakeable, không kéo cả lib vào bundle như moment.

## Lựa chọn khác (không dùng)

- **dayjs** — API kiểu chain giống moment (`dayjs().add(1, "day")`), bundle
  nhỏ hơn date-fns nếu chỉ cần vài hàm cơ bản, nhưng cần plugin cho
  locale/relative-time (`dayjs/plugin/relativeTime`).
- **luxon** — mạnh về timezone, nhưng nặng hơn, ít cần thiết trừ khi app xử
  lý nhiều timezone khác nhau.

## Cách đổi lib sau này

Không có điểm chặn — gọi trực tiếp `import {...} from "date-fns"` ở từng
file cần. Nếu muốn dễ đổi lib sau, có thể bọc qua 1 module `lib/date.ts` export
lại các hàm hay dùng (`formatDate`, `timeAgo`).
