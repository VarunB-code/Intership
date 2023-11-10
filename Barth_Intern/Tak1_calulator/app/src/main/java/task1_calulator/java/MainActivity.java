package task1_calulator.java;

        import android.content.Context;
        import android.graphics.drawable.GradientDrawable;
        import android.os.Bundle;
        import android.app.Activity;
        import android.view.View;
        import android.widget.Button;
        import android.widget.EditText;
        import android.widget.TextView;

public class MainActivity extends Activity {

    private EditText num1EditText;
    private EditText num2EditText;
    private TextView resultTextView;
    private Button addButton;
    private Button subtractButton;
    private Button multiplyButton;
    private Button divideButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1EditText = findViewById(R.id.num1_edit_text);
        num2EditText = findViewById(R.id.num2_edit_text);
        resultTextView = findViewById(R.id.result_text_view);
        addButton = findViewById(R.id.add_button);
        subtractButton = findViewById(R.id.subtract_button);
        multiplyButton = findViewById(R.id.multiply_button);
        divideButton = findViewById(R.id.divide_button);

        // Set the background gradient of the app
        GradientDrawable gradientDrawable = new GradientDrawable(
                GradientDrawable.Orientation.TOP_BOTTOM,
                new int[]{getResources().getColor(R.color.colorPrimary), getResources().getColor(R.color.colorPrimaryDark)}
        );
        getWindow().setBackgroundDrawable(gradientDrawable);

        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double num1 = Double.parseDouble(num1EditText.getText().toString());
                double num2 = Double.parseDouble(num2EditText.getText().toString());
                double result = num1 + num2;
                resultTextView.setText(String.format("%.2f", result));
            }
        });

        subtractButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double num1 = Double.parseDouble(num1EditText.getText().toString());
                double num2 = Double.parseDouble(num2EditText.getText().toString());
                double result = num1 - num2;
                resultTextView.setText(String.format("%.2f", result));
            }
        });

        multiplyButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double num1 = Double.parseDouble(num1EditText.getText().toString());
                double num2 = Double.parseDouble(num2EditText.getText().toString());
                double result = num1 * num2;
                resultTextView.setText(String.format("%.2f", result));
            }
        });

        divideButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double num1 = Double.parseDouble(num1EditText.getText().toString());
                double num2 = Double.parseDouble(num2EditText.getText().toString());
                double result = num1 / num2;
                resultTextView.setText(String.format("%.2f", result));
            }
        });
    }
}
