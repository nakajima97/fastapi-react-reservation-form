import "./App.css";
import { Box } from "@mui/system";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import "dayjs/locale/ja";
import * as dayjs from "dayjs";
import { Controller, useForm } from "react-hook-form";
import { Button, TextField } from "@mui/material";

dayjs.locale("ja");

function App() {
  const { register, control } = useForm();

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
        <Box>
          <TextField {...register("name")} />
        </Box>
        <Box>
          <TextField {...register("emailAddress")} />
        </Box>
        <Box>
          <TextField {...register("phoneNumber")} />
        </Box>
        <Button type="submit">Submit</Button>
      </LocalizationProvider>
    </>
  );
}

export default App;
