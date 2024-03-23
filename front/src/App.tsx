import "./App.css";
import { Box } from "@mui/system";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import "dayjs/locale/ja";
import * as dayjs from "dayjs";
import { Controller, useForm } from "react-hook-form";

dayjs.locale("ja");

function App() {
  const { control } = useForm();

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Box>
          <Controller
            name="date"
            control={control}
            render={({ field }) => <DatePicker {...field} />}
          />
        </Box>
      </LocalizationProvider>
    </>
  );
}

export default App;
